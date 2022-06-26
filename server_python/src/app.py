# -*- coding: utf-8 -*-
from ariadne import load_schema_from_path, make_executable_schema, snake_case_fallback_resolvers, graphql_sync, \
    ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS

from src.resolvers.mutations.auth_mutations import signup_mutation_resolver, signin_mutation_resolver
from src.resolvers.mutations.post_mutations import post_create_mutation_resolver, post_delete_mutation_resolver
from src.resolvers.type_resolvers.post_resolvers import post_author_resolver
from src.resolvers.type_resolvers.profile_resolvers import profile_user_resolver
from src.resolvers.query_resolvers import query_posts_resolver, query_me_resolver, query_users_resolver
from src.resolvers.type_resolvers.user_resolvers import user_profile_resolver, user_posts_resolver
from src.utils.token import extract_user_data_from_token

app = Flask(__name__)
CORS(app)

profile = ObjectType("Profile")
profile.set_field("user", profile_user_resolver)

post = ObjectType("Post")
post.set_field("author", post_author_resolver)

user = ObjectType("User")
user.set_field("profile", user_profile_resolver)
user.set_field("posts", user_posts_resolver)

query = ObjectType("Query")
query.set_field("posts", query_posts_resolver)
query.set_field("me", query_me_resolver)
query.set_field("users", query_users_resolver)

mutation = ObjectType("Mutation")
mutation.set_field("signUp", signup_mutation_resolver)
mutation.set_field("signIn", signin_mutation_resolver)
mutation.set_field("postCreate", post_create_mutation_resolver)
mutation.set_field("postDelete", post_delete_mutation_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, post, profile, user, snake_case_fallback_resolvers
)


def _get_context(req):
    token = req.headers.get("Authorization")
    return {
        "request": req,
        "user_info": extract_user_data_from_token(token) if token is not None else None
    }


@app.route("/", methods=["GET", ])
def index():
    return redirect(url_for("graphql_playground")), 302


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=_get_context(request),
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)

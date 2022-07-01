# -*- coding: utf-8 -*-
from ariadne import ObjectType, load_schema_from_path, make_executable_schema, snake_case_fallback_resolvers, \
    graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, redirect, url_for, jsonify, request
from flask_cors import CORS

from src.resolvers.mutation_resolvers.review_mutations import mutation_review_create_resolver, \
    mutation_review_delete_resolver
from src.resolvers.type_resolvers.product_resolver import product_review_resolver
from src.resolvers.type_resolvers.review_resolver import review_product_resolver
from src.settings import inc_request_count, get_request_count, LOGGER

from src.resolvers.query_resolvers import query_hello_resolver, query_myname_resolver, query_req_count_resolver, \
    query_products_resolver, query_review_resolver, query_product_resolver

app = Flask(__name__)
CORS(app)

query = ObjectType("Query")
query.set_field("hello", query_hello_resolver)
query.set_field("myName", query_myname_resolver)
query.set_field("reqCount", query_req_count_resolver)
query.set_field("products", query_products_resolver)
query.set_field("review", query_review_resolver)
query.set_field("product", query_product_resolver)

product = ObjectType("Product")
product.set_field("reviews", product_review_resolver)

review = ObjectType("Review")
review.set_field("product", review_product_resolver)

mutation = ObjectType("Mutation")
mutation.set_field("reviewCreate", mutation_review_create_resolver)
mutation.set_field("reviewDelete", mutation_review_delete_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, product, review, mutation, snake_case_fallback_resolvers
)


def _get_context(req):
    inc_request_count()
    return {
        "request": req,
        "request_count": get_request_count()
    }


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/", methods=["GET", ])
def index():
    return redirect(url_for("graphql_playground")), 302


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

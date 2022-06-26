# -*- coding: utf-8 -*-
from ariadne import convert_kwargs_to_snake_case

import src.services.post_service as post_service
import src.services.user_service as user_service
from src.models.payloads.error_item import ErrorItem
from src.models.payloads.posts_payload import PostsPayload
from src.models.payloads.user_payload import UserPayload
from src.models.payloads.users_payload import UsersPayload
from src.settings import LOGGER
from src.utils.payload_utils import log_errors


@convert_kwargs_to_snake_case
def query_posts_resolver(obj, info, skip: int = 0, take: int = 100) -> PostsPayload:
    LOGGER.info("Resolving: Query.posts")
    try:
        posts = post_service.post_get_paginated(skip=skip, take=take)
        log_errors(posts.errors, "Query.posts")
        return posts

    except Exception as e:
        return PostsPayload(errors=[ErrorItem(f"Failed to run resolver Query.posts: {e}")])


@convert_kwargs_to_snake_case
def query_me_resolver(obj, info) -> UserPayload:
    LOGGER.info("Resolving: Query.me")
    try:
        user_info = info.context["user_info"]
        if user_info is None:
            return UserPayload(errors=[ErrorItem("You must be logged in to fetch your information.")])

        my_profile = user_service.user_get(user_info.user_id)
        log_errors(my_profile.errors, "Query.me")
        return my_profile

    except Exception as e:
        return UserPayload(errors=[ErrorItem(f"Failed to run resolver Query.me: {e}")])


@convert_kwargs_to_snake_case
def query_users_resolver(obj, info, skip: int = 0, take: int = 100) -> UsersPayload:
    LOGGER.info("Resolving: Query.users")
    try:
        users = user_service.user_get_paginated(skip=skip, take=take)
        log_errors(users.errors, "Query.users")
        return users

    except Exception as e:
        return UsersPayload(errors=[ErrorItem(f"Failed to run resolver Query.users: {e}")])

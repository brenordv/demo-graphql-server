# -*- coding: utf-8 -*-
from typing import List
from ariadne import convert_kwargs_to_snake_case

from src.constants import DEFAULT_TAKE, DEFAULT_SKIP
from src.models.post import Post
from src.models.profile import Profile
from src.models.user import User
from src.settings import LOGGER
import src.services.profile_service as profile_service
import src.services.post_service as post_service
from src.utils.payload_utils import log_errors


@convert_kwargs_to_snake_case
def user_profile_resolver(obj: User, info) -> Profile:
    LOGGER.info("Resolving: User.profile")
    user_info = info.context["user_info"]
    logged_id = user_info.user_id if user_info is not None else None
    result = profile_service.profile_get(obj.id)
    log_errors(result.errors, "User.profile")
    profile = result.profile
    profile.is_own_profile = profile.user_id == logged_id
    return profile


@convert_kwargs_to_snake_case
def user_posts_resolver(obj: User, info) -> List[Post]:
    LOGGER.info("Resolving: User.posts")

    result = post_service.post_get_paginated_by_author(
        author_id=obj.id, skip=DEFAULT_SKIP, take=DEFAULT_TAKE
    )
    log_errors(result.errors, "User.posts")
    posts = result.posts
    return posts

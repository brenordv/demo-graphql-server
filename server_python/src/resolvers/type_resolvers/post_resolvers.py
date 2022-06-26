# -*- coding: utf-8 -*-
from ariadne import convert_kwargs_to_snake_case

from src.models.post import Post
from src.models.user import User
from src.settings import LOGGER
import src.services.user_service as user_service
from src.utils.payload_utils import log_errors


@convert_kwargs_to_snake_case
def post_author_resolver(obj: Post, info) -> User:
    LOGGER.info("Resolving: Post.author")
    result = user_service.user_get(obj.author_id)
    log_errors(result.errors, "Post.author")
    return result.user


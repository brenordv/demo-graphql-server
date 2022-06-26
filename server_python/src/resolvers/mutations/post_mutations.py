# -*- coding: utf-8 -*-
from ariadne import convert_kwargs_to_snake_case

from src.models.inputs.add_post_args import AddPostArgs
from src.models.inputs.base_add_post_args import BaseAddPostArgs
from src.models.payloads.error_item import ErrorItem
from src.models.payloads.post_payload import PostPayload
from src.settings import LOGGER
import src.services.post_service as post_service
from src.utils.payload_utils import log_errors


@convert_kwargs_to_snake_case
def post_create_mutation_resolver(obj, info, input: dict) -> PostPayload:
    LOGGER.info("Resolving: Mutation.postCreate")
    try:
        user_info = info.context["user_info"]
        if user_info is None:
            return PostPayload(errors=[ErrorItem("You must be logged in to create posts.")])
        post_data = BaseAddPostArgs(**input)
        result = post_service.post_insert(
            AddPostArgs(**post_data.__dict__, author_id=user_info.user_id)
        )

        log_errors(result.errors, "Mutation.postCreate")
        return result

    except Exception as e:
        return PostPayload(errors=[ErrorItem(f"Failed to run resolver Mutation.postCreate: {e}")])


@convert_kwargs_to_snake_case
def post_delete_mutation_resolver(obj, info, post_id: int) -> PostPayload:
    LOGGER.info("Resolving:  Mutation.postDelete")
    try:
        user_info = info.context["user_info"]
        if user_info is None:
            return PostPayload(errors=[ErrorItem("You must be logged in to delete posts.")])

        result = post_service.post_get_by_id(post_id)
        log_errors(result.errors, "Mutation.postDelete")
        post = result.post

        if post is None:
            return result

        if post.author_id != user_info.user_id:
            return PostPayload(errors=[ErrorItem("Hey smarty pants, this is not your post! You cannot delete it!")])

        delete_res = post_service.post_delete(post_id)
        if not delete_res.result:
            return PostPayload(errors=delete_res.errors)

        return PostPayload(post=post)
    except Exception as e:
        return PostPayload(errors=[ErrorItem(f"Failed to run resolver Mutation.postDelete: {e}")])

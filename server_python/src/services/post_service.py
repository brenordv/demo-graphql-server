# -*- coding: utf-8 -*-
from typing import Union, List

import src.repositories.post_repository as post_repo
from src.models.inputs.add_post_args import AddPostArgs
from src.models.payloads.bool_payload import BoolPayload
from src.models.payloads.error_item import ErrorItem
from src.models.payloads.post_payload import PostPayload
from src.models.payloads.posts_payload import PostsPayload
from src.utils.validations import validate_numeric_args


def _validate_add_post_args(data: AddPostArgs) -> Union[List[ErrorItem], None]:
    if data is None:
        return [ErrorItem("Input data cannot be null.")]

    if data.author_id < 0:
        return [ErrorItem("Author Id must be provided and must be valid.")]

    if data.title is None or data.title.strip() == "":
        return [ErrorItem("All posts must have a title.")]

    if data.content is None or data.content.strip() == "":
        return [ErrorItem("All posts must have a content.")]

    return None


def post_get_paginated(skip: int, take: int) -> PostsPayload:
    errors = validate_numeric_args({"skip": skip, "take": take}, 0)
    if errors is not None:
        return PostsPayload(errors=errors)

    try:
        return PostsPayload(posts=post_repo.post_get_paginated(skip=skip, take=take))
    except Exception as e:
        return PostsPayload(errors=[ErrorItem(f"Failed to get paginated posts: {e}")])


def post_get_paginated_by_author(author_id: int, skip: int, take: int) -> PostsPayload:
    errors = validate_numeric_args({"author_id": author_id, "skip": skip, "take": take}, 0)
    if errors is not None:
        return PostsPayload(errors=errors)

    try:
        return PostsPayload(posts=post_repo.post_get_paginated_by_author(author_id=author_id, skip=skip, take=take))
    except Exception as e:
        return PostsPayload(errors=[ErrorItem(f"Failed to get paginated posts by author: {e}")])


def post_insert(data: AddPostArgs) -> PostPayload:
    errors = _validate_add_post_args(data)
    if errors is not None:
        return PostPayload(errors=errors)

    try:
        return PostPayload(post=post_repo.post_insert(data))
    except Exception as e:
        return PostPayload(errors=[ErrorItem(f"Failed to insert post: {e}")])


def post_delete(post_id: int) -> BoolPayload:
    if post_id < 0:
        return BoolPayload(errors=[ErrorItem("A Post Id must be provided and must be a valid number.")])

    try:
        return BoolPayload(result=post_repo.post_delete(post_id))
    except Exception as e:
        return BoolPayload(errors=[ErrorItem(f"Failed to insert post: {e}")])


def post_get_by_id(post_id: int) -> PostPayload:
    if post_id < 0:
        return PostPayload(errors=[ErrorItem("A Post Id must be provided and must be a valid number.")])

    try:
        return PostPayload(post=post_repo.post_get(post_id))
    except Exception as e:
        return PostPayload(errors=[ErrorItem(f"Failed to get post by id: {e}")])

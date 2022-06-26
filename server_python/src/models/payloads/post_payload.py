# -*- coding: utf-8 -*-
from typing import List

from src.models.payloads.error_item import ErrorItem
from src.models.post import Post
from src.utils.payload_utils import parse_nullable_list


class PostPayload(object):
    def __init__(self, post: Post = None, errors: List[ErrorItem] = None) -> None:
        self.post: Post = post
        self.errors: List[ErrorItem] = parse_nullable_list(errors)

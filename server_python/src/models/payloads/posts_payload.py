# -*- coding: utf-8 -*-
from typing import List

from src.models.payloads.error_item import ErrorItem
from src.models.post import Post
from src.utils.payload_utils import parse_nullable_list


class PostsPayload(object):
    def __init__(self, posts: List[Post] = None, errors: List[ErrorItem] = None) -> None:
        self.posts: List[Post] = parse_nullable_list(posts)
        self.errors: List[ErrorItem] = parse_nullable_list(errors)

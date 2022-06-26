# -*- coding: utf-8 -*-
from src.models.inputs.base_add_post_args import BaseAddPostArgs


class AddPostArgs(BaseAddPostArgs):
    def __init__(self, title: str, content: str, author_id: int):
        super().__init__(title, content)
        self.author_id: int = author_id

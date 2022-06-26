# -*- coding: utf-8 -*-
from src.models.inputs.base_input import BaseInput


class BaseAddPostArgs(BaseInput):
    def __init__(self, title: str, content: str):
        self.title: str = title
        self.content: str = content

# -*- coding: utf-8 -*-
from src.models.inputs.base_input import BaseInput


class AddProfileArgs(BaseInput):
    def __init__(self, user_id: int, bio: str):
        self.user_id: int = user_id
        self.bio: str = bio

# -*- coding: utf-8 -*-
from src.models.inputs.base_input import BaseInput


class AddUserArgs(BaseInput):
    def __init__(self, name: str, username: str, password: str, email: str):
        self.name: str = name
        self.username: str = username
        self.password: str = password
        self.email: str = email

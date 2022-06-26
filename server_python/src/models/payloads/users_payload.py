# -*- coding: utf-8 -*-
from typing import List

from src.models.payloads.error_item import ErrorItem
from src.models.user import User
from src.utils.payload_utils import parse_nullable_list


class UsersPayload(object):
    def __init__(self, users: List[User] = None, errors: List[ErrorItem] = None) -> None:
        self.users: List[User] = users
        self.errors: List[ErrorItem] = parse_nullable_list(errors)

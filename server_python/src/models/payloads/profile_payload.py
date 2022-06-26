# -*- coding: utf-8 -*-
from typing import List

from src.models.payloads.error_item import ErrorItem
from src.models.profile import Profile
from src.utils.payload_utils import parse_nullable_list


class ProfilePayload(object):
    def __init__(self, profile: Profile = None, errors: List[ErrorItem] = None) -> None:
        self.profile: Profile = profile
        self.errors: List[ErrorItem] = parse_nullable_list(errors)

# -*- coding: utf-8 -*-
from typing import List

from src.models.payloads.error_item import ErrorItem
from src.utils.payload_utils import parse_nullable_list


class BoolPayload(object):
    def __init__(self, result: bool = None, errors: List[ErrorItem] = None) -> None:
        self.result: bool = result
        self.errors: List[ErrorItem] = parse_nullable_list(errors)

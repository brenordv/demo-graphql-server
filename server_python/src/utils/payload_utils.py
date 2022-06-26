# -*- coding: utf-8 -*-
from typing import List

from src.models.payloads.error_item import ErrorItem
from src.settings import LOGGER


def parse_nullable_list(obj):
    return obj if obj is not None else []


def log_errors(errors: List[ErrorItem], prefix: str) -> None:
    if errors is None or len(errors) == 0:
        return

    for err_msg in errors:
        LOGGER.error(f"[{prefix}: {err_msg.message}]")

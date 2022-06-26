# -*- coding: utf-8 -*-
from typing import Union, List

from src.models.payloads.error_item import ErrorItem


def validate_numeric_args(args: dict, min_value: int) -> Union[List[ErrorItem], None]:
    for key, val in args.items():
        if val >= min_value:
            continue
        return [ErrorItem(f"Parameter '{key}' must be informed and be greater than {min_value}.")]

    return None

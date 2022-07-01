# -*- coding: utf-8 -*-
import logging
from datetime import datetime

from simple_log_factory.log_factory import log_factory

LOGGER: logging = log_factory(log_name="GRAPHQL-SERVER", log_time_format="%H:%M:%S")
SERVER_VERSION = "1.0.0"
REQUEST_COUNT: int = 0


def inc_request_count():
    global REQUEST_COUNT
    REQUEST_COUNT += 1


def get_request_count():
    global REQUEST_COUNT
    return REQUEST_COUNT

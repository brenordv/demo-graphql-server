# -*- coding: utf-8 -*-
import logging

from simple_log_factory.log_factory import log_factory

LOGGER: logging = log_factory(log_name="GRAPHQL-SERVER", log_time_format="%H:%M:%S")

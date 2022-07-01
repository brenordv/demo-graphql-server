# -*- coding: utf-8 -*-
from typing import List, Union
from ariadne import convert_kwargs_to_snake_case

from src.data import PRODUCTS, REVIEWS
from src.settings import LOGGER, REQUEST_COUNT, SERVER_VERSION


@convert_kwargs_to_snake_case
def query_hello_resolver(obj, info, skip: int = 0, take: int = 100) -> str:
    LOGGER.info(f"Resolving: Query.hello | Query number={info.context.get('request_count')}")
    return "Hello, World!"


@convert_kwargs_to_snake_case
def query_myname_resolver(obj, info, my_name_is: str) -> str:
    LOGGER.info(f"Resolving: Query.myName | Query number={info.context.get('request_count')}")
    return f"Hi {my_name_is}! Nice to meet you!"


@convert_kwargs_to_snake_case
def query_req_count_resolver(obj, info) -> dict:
    LOGGER.info(f"Resolving: Query.reqCount | Query number={info.context.get('request_count')}")
    return {
        "count": REQUEST_COUNT,
        "server_version": SERVER_VERSION
    }


@convert_kwargs_to_snake_case
def query_products_resolver(obj, info) -> List[dict]:
    LOGGER.info(f"Resolving: Query.products | Query number={info.context.get('request_count')}")
    return [*PRODUCTS]


@convert_kwargs_to_snake_case
def query_review_resolver(obj, info, review_id: int) -> Union[dict, None]:
    LOGGER.info(f"Resolving: Query.review | Query number={info.context.get('request_count')}")
    filtered_reviews = [r for r in REVIEWS if r.get('id') == review_id]
    if len(filtered_reviews) == 0:
        return None

    return filtered_reviews[0]


@convert_kwargs_to_snake_case
def query_product_resolver(obj, info, product_id: str) -> Union[dict, None]:
    LOGGER.info(f"Resolving: Query.product({product_id}) | Query number={info.context.get('request_count')}")
    filtered_product = [p for p in PRODUCTS if p.get('id') == int(product_id)]
    if len(filtered_product) == 0:
        return None

    return filtered_product[0]

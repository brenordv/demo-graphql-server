# -*- coding: utf-8 -*-
from ariadne import convert_kwargs_to_snake_case

from src.data import PRODUCTS
from src.settings import LOGGER


@convert_kwargs_to_snake_case
def review_product_resolver(obj: dict, info) -> dict:
    LOGGER.info(f"Resolving: Review.product | Query number={info.context.get('request_count')}")
    product_id = obj.get("product_id")

    # No validation, but it's OK. We know that product exists.
    product = [p for p in PRODUCTS if p.get("id") == product_id][0]
    LOGGER.info(f"Product '{product.get('name')}' found for this review.")

    return product


# -*- coding: utf-8 -*-
from typing import List
from ariadne import convert_kwargs_to_snake_case

from src.data import REVIEWS
from src.settings import LOGGER


@convert_kwargs_to_snake_case
def product_review_resolver(obj: dict, info) -> List[dict]:
    LOGGER.info(f"Resolving: Product.reviews | Query number={info.context.get('request_count')}")
    product_id = obj.get("id")
    reviews = [r for r in REVIEWS if r["product_id"] == product_id]
    LOGGER.info(f"Found {len(reviews)} reviews for product {obj.get('name')}")

    return reviews

# -*- coding: utf-8 -*-
from typing import List

from src.data import REVIEWS
from src.settings import LOGGER


def product_review_resolver(obj: dict, info) -> List[dict]:
    LOGGER.info(f"Resolving: Product.reviews | Query number={info.context.get('request_count')}")
    product_id = obj.get("id")
    reviews = [r for r in REVIEWS if r["product_id"] == product_id]
    LOGGER.info(f"Found {len(reviews)} reviews for product {obj.get('name')}")

    return reviews

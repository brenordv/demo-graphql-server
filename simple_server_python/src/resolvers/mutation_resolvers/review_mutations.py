# -*- coding: utf-8 -*-
from datetime import datetime
from ariadne import convert_kwargs_to_snake_case

from src.data import PRODUCTS, REVIEWS
from src.settings import LOGGER


@convert_kwargs_to_snake_case
def mutation_review_create_resolver(obj, info, new_review_data: dict) -> dict:
    LOGGER.info(f"Resolving: Mutation.reviewCreate | Query number={info.context.get('request_count')}")

    product_id = int(new_review_data["product_id"])
    new_review_data["product_id"] = product_id

    if not any(p for p in PRODUCTS if p.get('id') == product_id):
        return {
            "success": False,
            "error_message": f"No product found with id '{product_id}'"
        }

    new_review_id = max([r["id"] for r in REVIEWS]) + 1
    REVIEWS.append({
        "id": new_review_id,
        "date_added": datetime.utcnow(),
        **new_review_data
    })

    return {
        "success": True,
        "review": REVIEWS[-1]
    }


@convert_kwargs_to_snake_case
def mutation_review_delete_resolver(obj, info: dict, review_id: str) -> dict:
    LOGGER.info(f"Resolving: Mutation.reviewDelete | Query number={info.context.get('request_count')}")
    rev_id = int(review_id)
    filtered_reviews = [r for r in REVIEWS if r.get('id') == rev_id]
    if len(filtered_reviews) == 0:
        return {
            "success": False,
            "error_message": f"No product found with id '{review_id}'"
        }

    review = filtered_reviews[0]
    REVIEWS.remove(review)

    return {
        "success": True,
        "review": review
    }

# -*- coding: utf-8 -*-
import jwt

from src.models.user import User
from src.models.user_info import UserInfo

JWT_SIGNATURE_KEY = "I know this should not be here. This should be in a very secure place, etc., but this is just an academic project..";


def generate_user_token(user: User):
    encoded_jwt = jwt.encode(
        payload={
            "user_id": user.id,
            "username": user.username
        },
        key=JWT_SIGNATURE_KEY,
        headers={
            "expiresIn": 86400 * 365  # 365 days. Again, I know it's not secure, but this is just a demo project.
        },
        algorithm="HS256")

    return encoded_jwt


def extract_user_data_from_token(token: str) -> UserInfo:
    payload = jwt.decode(token, JWT_SIGNATURE_KEY, algorithms="HS256")
    return UserInfo(**payload)

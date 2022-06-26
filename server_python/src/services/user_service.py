# -*- coding: utf-8 -*-
from typing import Union, List
import bcrypt

import src.repositories.user_repository as user_repo
from src.models.inputs.add_user_args import AddUserArgs
from src.models.payloads.auth_payload import AuthPayload
from src.models.payloads.error_item import ErrorItem
from src.models.payloads.user_payload import UserPayload
from src.models.payloads.users_payload import UsersPayload
from src.utils.token import generate_user_token
from src.utils.validations import validate_numeric_args


def _validate_add_user_args(data: AddUserArgs) -> Union[List[ErrorItem], None]:
    if data is None:
        return [ErrorItem("Input data cannot be null.")]

    if data.name is None or data.name.strip() == "":
        return [ErrorItem("Name cannot be null and must have 5 characters of more.")]

    if data.email is None or data.email.strip() == "" or not all([x in data.email for x in ["@", "."]]):
        return [ErrorItem("Email cannot be null and must have a valid format.")]

    if data.username is None or data.username.strip() == "" or data.username.startswith("@"):
        return [ErrorItem("Username cannot be null, must have 3 characters of more and cannot start with @.")]

    if data.password is None or data.password.strip() == "" or len(data.password) < 3:
        return [ErrorItem("Password cannot be null and must have 3 characters of more.")]

    return None


def user_insert(data: AddUserArgs) -> UserPayload:
    errors = _validate_add_user_args(data)
    if errors is not None:
        return UserPayload(errors=errors)

    try:
        return UserPayload(user=user_repo.user_insert(data))
    except Exception as e:
        return UserPayload(errors=[ErrorItem(f"Failed to insert user: {e}")])


def user_get(user_id: int) -> UserPayload:
    if user_id < 0:
        return UserPayload(errors=[ErrorItem("User Id cannot be null and must be greater than zero.")])

    try:
        return UserPayload(user=user_repo.user_get_by_id(user_id))
    except Exception as e:
        return UserPayload(errors=[ErrorItem(f"Failed to get user by Id: {e}")])


def user_login(username: str, password: str) -> AuthPayload:
    if username is None or username.strip() == '' or password is None or password.strip() == '':
        return AuthPayload(errors=[ErrorItem("Invalid credentials")])

    try:
        user = user_repo.user_get_by_username(username)
        if not bcrypt.checkpw(password.encode(encoding='utf-8'), user.password.encode(encoding='utf-8')):
            return AuthPayload(errors=[ErrorItem("Invalid credentials")])

        return AuthPayload(token=generate_user_token(user))
    except Exception as e:
        return AuthPayload(errors=[ErrorItem(f"Authentication failed: {e}")])


def user_get_paginated(skip: int, take: int) -> UsersPayload:
    errors = validate_numeric_args({"skip": skip, "take": take}, 0)
    if errors is not None:
        return UsersPayload(errors=errors)

    try:
        return UsersPayload(users=user_repo.user_get_paginated(skip=skip, take=take))
    except Exception as e:
        return UsersPayload(errors=[ErrorItem(f"Failed to get paginated users: {e}")])

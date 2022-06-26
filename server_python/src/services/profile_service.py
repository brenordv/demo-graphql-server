# -*- coding: utf-8 -*-
from typing import Union, List

import src.repositories.profile_repository as profile_repo
from src.models.inputs.add_profile_args import AddProfileArgs
from src.models.payloads.error_item import ErrorItem
from src.models.payloads.profile_payload import ProfilePayload
from src.models.profile import Profile


def _validate_add_profile_args(data: AddProfileArgs) -> Union[List[ErrorItem], None]:
    if data is None:
        return [ErrorItem("Input data cannot be null.")]

    if data.user_id < 0:
        return [ErrorItem("User Id must be provided and must be valid.")]

    if data.bio is None or data.bio.strip() == "":
        return [ErrorItem("A bio must be provided.")]

    return None


def profile_get(user_id: int) -> ProfilePayload:
    if user_id < 0:
        return ProfilePayload(errors=[ErrorItem("User Id must be provided and must be greater than zero.")])

    try:
        return ProfilePayload(profile=profile_repo.profile_get(user_id))
    except Exception as e:
        return ProfilePayload(errors=[ErrorItem(f"Failed to get user profile: {e}")])


def profile_insert(data: AddProfileArgs) -> ProfilePayload:
    errors = _validate_add_profile_args(data)
    if errors is not None:
        return ProfilePayload(errors=errors)

    try:
        return ProfilePayload(profile=profile_repo.profile_insert(data))
    except Exception as e:
        return ProfilePayload(errors=[ErrorItem(f"Failed to insert user profile: {e}")])


def profile_update(data: AddProfileArgs) -> ProfilePayload:
    errors = _validate_add_profile_args(data)
    if errors is not None:
        return ProfilePayload(errors=errors)

    try:
        return ProfilePayload(profile=profile_repo.profile_update(data))
    except Exception as e:
        return ProfilePayload(errors=[ErrorItem(f"Failed to update user profile: {e}")])


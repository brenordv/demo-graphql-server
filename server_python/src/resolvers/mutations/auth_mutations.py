# -*- coding: utf-8 -*-
from ariadne import convert_kwargs_to_snake_case

from src.models.inputs.add_profile_args import AddProfileArgs
from src.models.inputs.add_user_args import AddUserArgs
from src.models.payloads.auth_payload import AuthPayload
from src.models.payloads.error_item import ErrorItem
from src.settings import LOGGER
import src.services.user_service as user_service
import src.services.profile_service as profile_service
from src.utils.payload_utils import log_errors
from src.utils.token import generate_user_token


@convert_kwargs_to_snake_case
def signup_mutation_resolver(obj, info, input: dict, bio: str) -> AuthPayload:
    LOGGER.info("Resolving: Mutation.signUp")

    try:
        new_user_data = AddUserArgs(**input)
        user_res = user_service.user_insert(new_user_data)
        if user_res.user is None:
            log_errors(user_res.errors, "Mutation.signUp")
            return AuthPayload(errors=user_res.errors)

        user = user_res.user
        profile_res = profile_service.profile_insert(AddProfileArgs(user_id=user.id, bio=bio))
        if profile_res.profile is None:
            log_errors(profile_res.errors, "Mutation.signUp")
            return AuthPayload(errors=profile_res.errors)

        return AuthPayload(token=generate_user_token(user))
    except Exception as e:
        return AuthPayload(errors=[ErrorItem(f"Failed to run resolver Mutation.signUp: {e}")])


@convert_kwargs_to_snake_case
def signin_mutation_resolver(obj, info, username: str, password: str) -> AuthPayload:
    LOGGER.info("Resolving: Mutation.signIn")
    try:
        result = user_service.user_login(username, password)
        log_errors(result.errors, "Mutation.signIn")
        return result
    except Exception as e:
        return AuthPayload(errors=[ErrorItem(f"Failed to run resolver Mutation.signIn: {e}")])

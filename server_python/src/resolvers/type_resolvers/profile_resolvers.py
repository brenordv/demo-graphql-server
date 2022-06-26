# -*- coding: utf-8 -*-
from ariadne import convert_kwargs_to_snake_case

from src.models.profile import Profile
from src.models.user import User
from src.settings import LOGGER
import src.services.user_service as user_service
from src.utils.payload_utils import log_errors


@convert_kwargs_to_snake_case
def profile_user_resolver(obj: Profile, info) -> User:
    LOGGER.info("Resolving: Profile.user")
    result = user_service.user_get(obj.user_id)
    log_errors(result.errors, "Profile.user")
    return result.user


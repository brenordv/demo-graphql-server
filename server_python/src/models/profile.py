# -*- coding: utf-8 -*-
from datetime import datetime


class Profile(object):
    def __init__(self, id: int, bio: str, user_id: int,
                 created_at: datetime, updated_at: datetime,
                 is_own_profile: bool = False):
        self.id: int = id
        self.bio: str = bio
        self.user_id: int = user_id
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at
        self.is_own_profile: bool = is_own_profile

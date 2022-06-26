# -*- coding: utf-8 -*-
from datetime import datetime


class User(object):
    def __init__(self, id: int, name: str, username: str, password: str, email: str, created_at: datetime,
                 updated_at: datetime):
        self.id: int = id
        self.name: str = name
        self.username: str = username
        self.password: str = password
        self.email: str = email
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at

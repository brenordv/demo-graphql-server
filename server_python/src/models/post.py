# -*- coding: utf-8 -*-
from datetime import datetime


class Post(object):
    def __init__(self, id: int, title: str, content: str, author_id: int, created_at: datetime):
        self.id: int = id
        self.title: str = title
        self.content: str = content
        self.author_id: int = author_id
        self.created_at: datetime = created_at

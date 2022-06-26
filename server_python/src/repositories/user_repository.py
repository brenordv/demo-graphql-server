# -*- coding: utf-8 -*-
from typing import List

import bcrypt

from src.models.inputs.add_user_args import AddUserArgs
from src.models.user import User
from src.repositories.database import get_sqlite_conn, parse_row
from src.settings import LOGGER

INSERT_USER = "INSERT INTO users (name, username, email, password) VALUES (:name, :username, :email, :password)"
SELECT_USER = """
SELECT 
    id, 
    name, 
    username,
    password, 
    email,
    datetime(created_at, 'localtime') as created_at, 
    datetime(updated_at, 'localtime') as updated_at
FROM users"""

SELECT_USER_BY_ID = f"{SELECT_USER} WHERE id = :user_id"
SELECT_USER_BY_USERNAME = f"{SELECT_USER} WHERE username = :username"
SELECT_USER_PAGINATED = f"{SELECT_USER} ORDER BY username DESC LIMIT :take OFFSET :skip"


def _get_user(query, args) -> User:
    db = get_sqlite_conn()
    cursor = db.cursor()
    cursor.execute(query, args)
    rows = cursor.fetchall()
    if len(rows) == 0:
        raise ValueError(f"No user found for: {args}")
    user: User = parse_row(rows[0], cursor.description, User)
    cursor.close()
    return user


def user_get_by_id(user_id: int) -> User:
    LOGGER.info(f"Getting user by id: {user_id}")
    return _get_user(SELECT_USER_BY_ID, {"user_id": user_id})


def user_get_by_username(username: str) -> User:
    LOGGER.info(f"Getting user by username: {username}")
    return _get_user(SELECT_USER_BY_USERNAME, {"username": username})


def user_insert(data: AddUserArgs) -> User:
    LOGGER.info(f"User insert: {data}")

    salt = bcrypt.gensalt(rounds=10)
    hashed = bcrypt.hashpw(data.password.encode(encoding="utf-8"), salt)
    data.password = hashed.decode(encoding="utf-8")

    db = get_sqlite_conn()
    cursor = db.cursor()
    cursor.execute(INSERT_USER, data.__dict__)
    user_id = cursor.lastrowid
    db.commit()
    cursor.close()
    return user_get_by_id(user_id)


def user_get_paginated(skip: int, take: int) -> List[User]:
    LOGGER.info(f"User get paginated. Skip: {skip} | Take: {take}")
    db = get_sqlite_conn()

    users = []
    cursor = db.cursor()
    cursor.execute(SELECT_USER_PAGINATED, {"skip": skip, "take": take})
    rows = cursor.fetchall()
    for row in rows:
        users.append(parse_row(row, cursor.description, User))
    cursor.close()
    return users

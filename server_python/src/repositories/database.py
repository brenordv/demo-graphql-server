# -*- coding: utf-8 -*-
import sqlite3
from pathlib import Path
from sqlite3 import Connection
from typing import Union

from src.settings import LOGGER

_CREATE_USERS = """
CREATE TABLE IF NOT EXISTS users (
    id         integer
        constraint users_pk
            primary key autoincrement,
    name       text not null,
    username   text not null,
    email      text not null,
    password   text not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP
)
"""

_CREATE_UNIQUE_IX_USERS_USERNAME = "CREATE UNIQUE INDEX IF NOT EXISTS users_username_uindex ON USERS (username)"
_CREATE_UNIQUE_IX_USERS_EMAIL = "CREATE UNIQUE INDEX IF NOT EXISTS users_email_uindex ON USERS (email)"

_CREATE_PROFILES = """
CREATE TABLE IF NOT EXISTS profiles
(
    id      integer
        constraint profiles_pk
            primary key autoincrement,
    user_id integer
        constraint profiles_users_id_fk
            references users,
    bio     text not null,    
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP)"""

_CREATE_UNIQUE_IX_PROFILES_USER_ID = "CREATE UNIQUE INDEX IF NOT EXISTS profiles_user_id_uindex ON PROFILES (user_id)"

_CREATE_POSTS = """
CREATE TABLE IF NOT EXISTS posts
(
    id        integer
        constraint posts_pk
            primary key autoincrement,
    title     text not null,
    content   text not null,
    author_id integer
        constraint posts_users_id_fk
            references users,
    created_at timestamp default CURRENT_TIMESTAMP)"""

_CREATE_BASE_QUERIES = [
    _CREATE_USERS,
    _CREATE_UNIQUE_IX_USERS_USERNAME,
    _CREATE_UNIQUE_IX_USERS_EMAIL,
    _CREATE_PROFILES,
    _CREATE_UNIQUE_IX_PROFILES_USER_ID,
    _CREATE_POSTS
]

_DB_INITIALIZED = False
_CURRENT_DB: Union[Connection, None] = None


def get_sqlite_file() -> Path:
    return Path(__file__).parent.parent.parent.parent.joinpath(".app-data").joinpath("database.db")


def get_sqlite_conn() -> Connection:
    global _CREATE_BASE_QUERIES
    global _DB_INITIALIZED
    global _CURRENT_DB

    if _CURRENT_DB is None:
        db_file: Path = get_sqlite_file()
        sqlite3.register_converter("BOOLEAN", lambda v: bool(int(v)))
        _CURRENT_DB = sqlite3.connect(
            db_file,
            check_same_thread=False,
            detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

    if not _DB_INITIALIZED:
        cursor = _CURRENT_DB.cursor()
        for query in _CREATE_BASE_QUERIES:
            try:
                cursor.execute(query)
            except sqlite3.Error as e:
                LOGGER.error(f"Error running query: {query} | Error: {e}")
                raise
        _DB_INITIALIZED = True

    return _CURRENT_DB


def parse_row(row, description, model):
    parsed = {}
    columns = [d[0] for d in description]
    for col_name, col_value in zip(columns, row):
        parsed[col_name] = col_value

    return model(**parsed)

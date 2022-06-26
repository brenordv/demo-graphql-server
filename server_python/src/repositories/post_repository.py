# -*- coding: utf-8 -*-
from typing import List

from src.models.inputs.add_post_args import AddPostArgs
from src.models.post import Post
from src.repositories.database import get_sqlite_conn, parse_row
from src.settings import LOGGER

DELETE_POST = "DELETE FROM posts WHERE id = :post_id"
INSERT_POST = "INSERT INTO posts (title, content, author_id) VALUES (:title, :content, :author_id)"
SELECT_POST = """
SELECT
    id,
    title,
    content,
    author_id,
    datetime(created_at, 'localtime') as created_at
FROM posts"""
SELECT_POST_BY_POST_ID = f"{SELECT_POST} WHERE id = :post_id"
SELECT_POST_PAGINATED = f"{SELECT_POST} ORDER BY created_at DESC LIMIT :take OFFSET :skip"
SELECT_POST_PAGINATED_BY_AUTHOR = f"""
{SELECT_POST} WHERE author_id = :author_id ORDER BY created_at DESC LIMIT :take OFFSET :skip
"""


def post_get(post_id: int) -> Post:
    LOGGER.info(f"Getting post by its Id. Post Id: {post_id}")
    db = get_sqlite_conn()
    cursor = db.cursor()
    cursor.execute(SELECT_POST_BY_POST_ID, [post_id])
    rows = cursor.fetchall()
    if len(rows) == 0:
        raise ValueError(f"No post found for post id: {post_id}")
    post: Post = parse_row(rows[0], cursor.description, Post)
    cursor.close()
    return post


def post_insert(data: AddPostArgs) -> Post:
    LOGGER.info(f"Inserting Post: [{data.author_id}] {data.title}")
    db = get_sqlite_conn()
    cursor = db.cursor()
    cursor.execute(INSERT_POST, data.__dict__)
    post_id = cursor.lastrowid
    db.commit()
    cursor.close()
    return post_get(post_id)


def _post_get_paginated(query: str, args: dict) -> List[Post]:
    db = get_sqlite_conn()
    cursor = db.cursor()
    posts = []
    cursor.execute(query, args)
    rows = cursor.fetchall()
    for row in rows:
        posts.append(parse_row(row, cursor.description, Post))
    cursor.close()
    return posts


def post_get_paginated(skip: int, take: int) -> List[Post]:
    LOGGER.info(f"Getting paginated posts. Skip: {skip} | Take: {take}")
    return _post_get_paginated(SELECT_POST_PAGINATED, {"skip": skip, "take": take})


def post_get_paginated_by_author(author_id: int, skip: int, take: int) -> List[Post]:
    LOGGER.info(f"Getting paginated posts. Author Id: {author_id} | Skip: {skip} | Take: {take}")
    return _post_get_paginated(SELECT_POST_PAGINATED_BY_AUTHOR, {"author_id": author_id, "skip": skip, "take": take})


def post_delete(post_id: int) -> bool:
    LOGGER.info(f"Deleting post with id: ${post_id}")
    db = get_sqlite_conn()
    cursor = db.cursor()
    cursor.execute(DELETE_POST, {"post_id": post_id})
    db.commit()
    cursor.close()
    return cursor.rowcount == 1

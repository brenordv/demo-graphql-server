# -*- coding: utf-8 -*-
from src.models.inputs.add_profile_args import AddProfileArgs
from src.models.profile import Profile
from src.repositories.database import get_sqlite_conn, parse_row
from src.settings import LOGGER

INSERT_PROFILE = "INSERT INTO profiles (user_id, bio) VALUES (:user_id, :bio)"
UPDATE_PROFILE = "UPDATE profiles SET bio = :bio, updated_at = :updated_at WHERE user_id = :user_id"
SELECT_PROFILE = """
SELECT 
    id, 
    bio, 
    user_id as user_id,
    datetime(created_at, 'localtime') as created_at,     
    datetime(updated_at, 'localtime') as updated_at
    FROM profiles 
WHERE user_id = :user_id"""


def profile_get(user_id: int) -> Profile:
    LOGGER.info(f"Fetching profile for user Id: {user_id}")
    db = get_sqlite_conn()
    cursor = db.cursor()
    cursor.execute(SELECT_PROFILE, {"user_id": user_id})
    rows = cursor.fetchall()
    if len(rows) == 0:
        raise ValueError(f"No profile found profile for id {user_id}")
    profile: Profile = parse_row(rows[0], cursor.description, Profile)
    cursor.close()
    return profile


def profile_insert(data: AddProfileArgs) -> Profile:
    LOGGER.info(f"Inserting profile: {data}")
    db = get_sqlite_conn()
    cursor = db.cursor()
    cursor.execute(INSERT_PROFILE, data.__dict__)
    db.commit()
    cursor.close()
    return profile_get(data.user_id)


def profile_update(data: AddProfileArgs) -> Profile:
    LOGGER.info(f"Updating profile for userId: {data.user_id}")
    db = get_sqlite_conn()
    cursor = db.cursor()
    cursor.execute(UPDATE_PROFILE, data.__dict__)
    db.commit()
    cursor.close()
    return profile_get(data.user_id)

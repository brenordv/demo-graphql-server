import {getDatabase} from "./base";
import {Profile} from "../models/profile";
import {AddProfileArgs} from "../interfaces/profile-interfaces";
import {logger} from "../utils/log-utils";

const INSERT_PROFILE = `INSERT INTO profiles (user_id, bio) VALUES (@userId, @bio)`;
const UPDATE_PROFILE = `UPDATE profiles SET bio = @bio, updated_at = @updatedAt WHERE user_id = @userId`;
const SELECT_PROFILE = `
SELECT 
    id, 
    bio, 
    user_id as userId,
    strftime('%s', datetime(created_at, 'localtime')) as createdAt,     
    strftime('%s', datetime(updated_at, 'localtime')) as updatedAt
    FROM profiles 
WHERE user_id = @userId`;

export const profileInsert = (data: AddProfileArgs): Profile => {
    logger.verbose(`Inserting profile: ${data}`);
    const db = getDatabase();

    const insert = db.prepare(INSERT_PROFILE);
    insert.run(data);
    return profileGet(data.userId);
};

export const profileUpdate = (data: AddProfileArgs): Profile => {
    logger.verbose(`Updating profile for userId:: ${data.userId}`);
    const db = getDatabase();
    const update = db.prepare(UPDATE_PROFILE);
    const updatePayload = {
        ...data,
        updatedAt: new Date().toISOString()
    }
    update.run(updatePayload);

    return profileGet(data.userId);
};

export const profileGet = (userId: number): Profile => {
    logger.verbose(`Fetching profile for user Id: ${userId}`);
    const db = getDatabase();
    const select = db.prepare(SELECT_PROFILE);
    const profile = select.get({userId});

    profile.createdAt = new Date((+profile.createdAt)*1000);
    profile.updatedAt = new Date((+profile.updatedAt)*1000);

    return profile as Profile;
}
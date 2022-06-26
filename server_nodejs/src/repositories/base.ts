import {logger} from "../utils/log-utils";

const path = require('path');
const Database = require('better-sqlite3');

const dbPath = path.join(__dirname, '..','..','..', '.app-data', 'database.db');
const db = new Database(dbPath, { verbose: logger.debug });


const CREATE_USERS = `
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
)`;

const CREATE_UNIQUE_IX_USERS_USERNAME = "CREATE UNIQUE INDEX IF NOT EXISTS users_username_uindex ON USERS (username)";
const CREATE_UNIQUE_IX_USERS_EMAIL = "CREATE UNIQUE INDEX IF NOT EXISTS users_email_uindex ON USERS (email)";

const CREATE_PROFILES = `
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
    updated_at timestamp default CURRENT_TIMESTAMP)`;

const CREATE_UNIQUE_IX_PROFILES_USER_ID = "CREATE UNIQUE INDEX IF NOT EXISTS profiles_user_id_uindex ON PROFILES (user_id)";

const CREATE_POSTS = `
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
    created_at timestamp default CURRENT_TIMESTAMP)`;

const CREATE_DB: string[] = [
    CREATE_USERS,
    CREATE_UNIQUE_IX_USERS_EMAIL,
    CREATE_UNIQUE_IX_USERS_USERNAME,
    CREATE_PROFILES,
    CREATE_UNIQUE_IX_PROFILES_USER_ID,
    CREATE_POSTS
];

let db_initialized = false;

export const getDatabase = () => {
    if (!db_initialized) {
        CREATE_DB.forEach((sql: string) => db.exec(sql, (err: Error) => {
            if (!err) return;
            logger.error(`Error running query: ${sql} | Error: ${err}`);
            throw err;
        }));
        db_initialized = true;
    }

    return db;
};
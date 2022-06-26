import {User} from "../models/user";
import {AddUserArgs} from "../interfaces/user-interfaces";
import bcrypt from "bcryptjs";
import {getDatabase} from "./base";
import {logger} from "../utils/log-utils";

const INSERT_USER = `INSERT INTO users (name, username, email, password) VALUES (@name, @username, @email, @password)`;
const SELECT_USER = `
SELECT 
    id, 
    name, 
    username,
    password, 
    email,
    strftime('%s', datetime(created_at, 'localtime')) as createdAt, 
    strftime('%s', datetime(updated_at, 'localtime')) as updatedAt
FROM users`;

const SELECT_USER_BY_ID = `${SELECT_USER} WHERE id = @userId`;
const SELECT_USER_BY_USERNAME = `${SELECT_USER} WHERE username = @username`;
const SELECT_USER_PAGINATED = `${SELECT_USER} ORDER BY username DESC LIMIT @take OFFSET @skip`;

const parseUser = (data: any): User => {
    const user = {...data};
    user.createdAt = new Date((+user.createdAt)*1000);
    user.updatedAt = new Date((+user.updatedAt)*1000);
    return user;
}


export const userInsert = (data: AddUserArgs): User => {
    logger.verbose(`User insert: ${data}`);
    const db = getDatabase();
    data.password = bcrypt.hashSync(data.password, 10);

    const insert = db.prepare(INSERT_USER);
    const {lastInsertRowid} = insert.run(data);

    return userGet(lastInsertRowid);
};

export const userGet = (userId: number): User => {
    logger.verbose(`Getting user by id: ${userId}`);
    const db = getDatabase();
    const select = db.prepare(SELECT_USER_BY_ID)
    const user = select.get({userId});
    return parseUser(user);
}

export const userGetByUsername = (username: string): User => {
    logger.verbose(`User get by username. Username: ${username}`);
    const db = getDatabase();
    const select = db.prepare(SELECT_USER_BY_USERNAME)
    const user = select.get({username});
    return parseUser(user);
}

export const userGetPaginated = (skip: number = 0, take: number = 100): User[] => {
    logger.verbose(`User get paginated. Skip: ${skip} | Take: ${take}`);
    const db = getDatabase();
    const select = db.prepare(SELECT_USER_PAGINATED);
    const users: User[] = [];
    select.all({skip, take}).forEach((u:any) => {
        users.push(parseUser(u));
    });
    return users;
}
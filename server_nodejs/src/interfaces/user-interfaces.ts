import {User} from "../models/user";
import {AuthPayload} from "./auth-interfaces";
import {BasePayloadInterface} from "./base-payload-interface";

export interface AddUserArgs {
    name: string,
    username: string,
    email: string,
    password: string
}

export interface InputAddUserArgs {
    input: AddUserArgs,
    bio: string
}

export interface UsersPayload extends BasePayloadInterface {
    users?: User[]
}

export interface UserPayload extends BasePayloadInterface {
    user?: User | null
}

export interface UserService {
    userInsert(data: AddUserArgs): UserPayload,
    userGet(authorId: number): UserPayload,
    userLogin(username:string, password: string): Promise<AuthPayload>
    userGetPaginated(skip: number, take: number): UsersPayload
}
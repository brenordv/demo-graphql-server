import {AddUserArgs, UserPayload, UserService, UsersPayload} from "../interfaces/user-interfaces";
import validator from "validator";
import * as userRepo from '../repositories/user-repository';
import {AuthPayload} from "../interfaces/auth-interfaces";
import bcrypt from "bcryptjs";
import {generateToken} from "../utils/jwt-utils";
import {logger} from "../utils/log-utils";
import {DEFAULT_SKIP, DEFAULT_TAKE} from "../constants/pagination-constants";

const userInsert = (data: AddUserArgs): UserPayload => {
    if (!data)
        return {
            errors: [{message:"Input data cannot be null."}],
        }


    if (!data.name || !validator.isLength(data.name, {min: 5}))
        return {
            errors: [{message:"Name cannot be null and must have 5 characters of more."}],
        }

    if (!data.email || !validator.isEmail(data.email))
        return {
            errors: [{message:"Email cannot be null and must have a valid format."}],
        }


    if (!data.username || !validator.isLength(data.username, {min: 3}))
        return {
            errors: [{message:"Username cannot be null and must have 3 characters of more."}],
        }

    if (data.username.startsWith("@"))
        return {
            errors: [{message:"Username cannot start with @."}],
        }

    if (!data.password || !validator.isLength(data.password, {min: 3}))
        return {
            errors: [{message:"Password cannot be null and must have 3 characters of more."}],
        }


    try {
        return {
            errors: [],
            user: userRepo.userInsert(data)
        };
    }catch (e) {
        return {
            errors: [{message:`Failed to add User: ${data} | Error: ${e}`}],
            user: null
        }
    }
};

const userGet = (userId: number): UserPayload => {
    if (!userId || userId < 0)
        return {
            errors: [{message:"User Id cannot be null and must be greater than zero."}],
        }

    try {
        return {
            errors: [],
            user: userRepo.userGet(userId)
        }
    }catch (e) {
        return {
            errors: [{message:"Failed to get User." + e}],
            user: null
        }
    }
}

const userLogin = async (username:string, password: string): Promise<AuthPayload> => {
    try {
        const user = userRepo.userGetByUsername(username);
        if (!await bcrypt.compare(password, user.password))
            return {
                errors: [{message: "Invalid credentials."}]
            }

        return {
            errors: [],
            token: generateToken(user)
        }
    }catch (e) {
        logger.error(`UserService Error: ${e}`);
        return {
            errors: [{message:"Invalid Credentials."}],
        }
    }

}

const userGetPaginated = (skip: number = DEFAULT_SKIP, take: number = DEFAULT_TAKE): UsersPayload => {
    try {
        if (skip < 0)
            return {
                errors: [{message: "Skip cannot be null and must be greater than zero."}]
            }

        if (take < 0)
            return {
                errors: [{message: "Take cannot be null and must be greater than zero."}]
            }

        return {
            errors: [],
            users: userRepo.userGetPaginated(skip, take)
        }

    } catch (e) {
        return {
            errors: [{message:`Error fetching paginated users. ${e}`}],
        }
    }
}

export const userService: UserService = {
    userInsert,
    userGet,
    userLogin,
    userGetPaginated
}
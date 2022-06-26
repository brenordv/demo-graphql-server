import {User, UserInfo} from "../models/user";
import JWT from "jsonwebtoken";
import {JWT_SIGNATURE_KEY} from "../secrets";

export const generateToken = (user: User): string => {
    return JWT.sign({
            userId: user.id,
            username: user.username
        },
        JWT_SIGNATURE_KEY,
        {
            expiresIn: 86400 * 365 // 365 days. Again, I know it's not secure, but this is just a demo project.
        });
}

export const getUserFromToken = (token: string | null | undefined): UserInfo | null => {
    if (!token)
        return null;

    try {
        return JWT.verify(token, JWT_SIGNATURE_KEY) as UserInfo;
    } catch (e) {
        return null;
    }
}
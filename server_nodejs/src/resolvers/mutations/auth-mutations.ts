import {GraphqlContext} from "../../interfaces/graphql-context";
import {InputAddUserArgs} from "../../interfaces/user-interfaces";
import {AuthPayload} from "../../interfaces/auth-interfaces";
import {generateToken} from "../../utils/jwt-utils";
import {logErrorMessages, logger} from "../../utils/log-utils";


export const authResolvers = {
    signUp: (_: any, {input, bio}: InputAddUserArgs, {userService, profileService}: GraphqlContext): AuthPayload => {
        logger.verbose(`Resolving: Mutation.signUp.`);

        const response = userService.userInsert({...input});

        if (!response.user) {
            logErrorMessages(response.errors);
            return {
                errors: response.errors
            }
        }

        const {user} = response;
        const profileInsertResult = profileService.profileInsert({
            userId: user.id,
            bio
        })

        if (!profileInsertResult.profile) {
            logErrorMessages(profileInsertResult.errors);
            return {errors: profileInsertResult.errors};
        }

        return {
            errors: [],
            token: generateToken(user)
        }
    },
    signIn: async (_: any, {username, password}: { username: string, password: string }, {userService}: GraphqlContext): Promise<AuthPayload> => {
        logger.verbose("Resolving: Mutation.signIn");
        const result = await userService.userLogin(username, password);

        if (!result.token)
            logErrorMessages(result.errors);
        return result;
    }
}
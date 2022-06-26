import {GraphqlContext} from "../interfaces/graphql-context";
import {Profile as ProfileModel} from "../models/profile";
import {logErrorMessages, logger} from "../utils/log-utils";

export const Profile = {
    user: ({userId}: ProfileModel, __: any, {userService}: GraphqlContext) => {
        logger.verbose("Resolving: Profile.user");

        const result = userService.userGet(userId);
        logErrorMessages(result.errors);

        return result.user;
    },
}
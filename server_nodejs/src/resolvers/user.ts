import {User as UserModel} from "../models/user";
import {GraphqlContext} from "../interfaces/graphql-context";
import {DEFAULT_SKIP, DEFAULT_TAKE} from "../constants/pagination-constants";
import {logErrorMessages, logger} from "../utils/log-utils";

export const User = {
    profile: ({id}: UserModel, __: any, {profileService, userInfo}: GraphqlContext) => {
        logger.verbose("Resolving: User.profile");

        const result = profileService.profileGet(id);
        logErrorMessages(result.errors);
        const {profile} = profileService.profileGet(id);

        return {
            ...profile,
            itsOwn: profile?.userId === userInfo.userId
        };
    },

    posts: ({id}: UserModel, __: any, {postService}: GraphqlContext) => {
        logger.verbose("Resolving: User.posts");

        const result = postService.postGetPaginatedByAuthor(id, DEFAULT_SKIP, DEFAULT_TAKE);
        logErrorMessages(result.errors);

        return result.posts;
    },
}


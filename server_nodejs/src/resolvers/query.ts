import {GraphqlContext} from "../interfaces/graphql-context";
import {logErrorMessages, logger} from "../utils/log-utils";

export const Query = {
    posts: async (_: any, {skip, take}: { skip: number, take: number }, {postService}: GraphqlContext) => {
        logger.verbose("Resolving: Query.posts");

        const response = postService.postGetPaginated(skip, take);
        logErrorMessages(response.errors);

        return response;
    },
    me: async (_: any, __: any, {userService, userInfo}: GraphqlContext) => {
        logger.verbose("Resolving: Query.me");

        const response = userService.userGet(userInfo.userId);
        logErrorMessages(response.errors);

        return response;
    },
    users: async (_: any, {skip, take}: { skip: number, take: number }, {userService}: GraphqlContext) => {
        logger.verbose("Resolving: Query.users");

        const response = userService.userGetPaginated(skip, take);
        console.log(response);
        logErrorMessages(response.errors);

        return response;
    },
}
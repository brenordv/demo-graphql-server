import {Post as PostModel } from "../models/post";
import {GraphqlContext} from "../interfaces/graphql-context";
import {logErrorMessages, logger} from "../utils/log-utils";

export const Post = {
    author: ({authorId}: PostModel, __: any, {userService}: GraphqlContext) => {
        logger.verbose("Resolving: Post.author");

        const result = userService.userGet(authorId);
        logErrorMessages(result.errors);
        const {user} = result;

        return user;
    },
}
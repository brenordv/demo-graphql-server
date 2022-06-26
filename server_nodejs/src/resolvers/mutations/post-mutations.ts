import {InputAddPostArgs, PostPayload} from "../../interfaces/post-interfaces";
import {GraphqlContext} from "../../interfaces/graphql-context";
import {logErrorMessages, logger} from "../../utils/log-utils";

export const postResolvers = {
    postCreate: (_: any, {input}:InputAddPostArgs, {postService, userInfo}: GraphqlContext): PostPayload => {
        logger.verbose("Resolving: Mutation.postCreate");

        const result = postService.postInsert({
            ...input,
            authorId: userInfo.userId
        });
        logErrorMessages(result.errors);

        return result;
    },
    postDelete: (_: any, {postId}: {postId: number}, {postService, userInfo}: GraphqlContext): PostPayload => {
        logger.verbose("Resolving: Mutation.postDelete");
        let errMsg: string;
        if (!userInfo)
        {
            errMsg = "You must be authenticated to use this route.";
            logger.error(errMsg);
            return {
                errors: [{message: errMsg}]
            }
        }

        const result = postService.postGetByPostId(postId);
        if (!result.post) {
            logErrorMessages(result.errors);
            return result;
        }

        const {post} = result;
        if (post.authorId !== userInfo.userId)
        {
            errMsg = "This is not your post. You cannot delete it.";
            logger.error(errMsg);
            return {
                errors: [{message: errMsg}]
            }
        }

        const deleteResult = postService.postDelete(postId);
        if (!deleteResult.result) {
            logErrorMessages(deleteResult.errors);
            return {
                errors: deleteResult.errors
            }
        }

        return result;
    }
}
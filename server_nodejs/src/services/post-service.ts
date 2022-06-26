import * as postRepo from "../repositories/post-repository";
import {AddPostArgs, PostPayload, PostService} from "../interfaces/post-interfaces";
import {BooleanPayload} from "../interfaces/boolean-interfaces";

const validateAddPostArgs = (data: AddPostArgs):PostPayload | null => {
    if (!data)
        return {errors: [{message: "Input data cannot be null."}],}

    if (!data.authorId || data.authorId < 0)
        return {errors: [{message: "Author Id must be provided and must be valid."}],}

    if (!data.title)
        return {errors: [{message: "All posts must have a title."}],}

    if (!data.content)
        return {errors: [{message: "All posts must have content."}],}

    return null;
}

const postInsert = (data: AddPostArgs): PostPayload => {
    const error = validateAddPostArgs(data);
    if (error) return error;

    try {
        return {
            errors: [],
            post: postRepo.postInsert(data)
        };
    } catch (e) {
        return {
            errors: [{message: "Failed to add Post." + e}],
        }
    }
};

const postDelete = (postId: number): BooleanPayload => {
    if (!postId || Number.isNaN(postId) || postId < 0)
        return {
            errors: [{message: "A Post Id must be provided and must be a valid number."}],
            result: false
        }

    try {
        return {
            errors: [],
            result: postRepo.postDelete(postId)
        };
    } catch (e) {
        return {
            errors: [{message: "Failed to delete Post." + e}],
            result: false
        }
    }
}

const postGetPaginated = (skip: number = 0, take: number = 100): PostPayload => {
    if (skip < 0 || take < 0)
        return {
            errors: [{message: "Skip and Take parameters must be greater than zero."}]
        }

    try {
        return {
            errors: [],
            posts: postRepo.postGetPaginated(skip, take)
        }
    } catch (e) {
        return {
            errors: [{message: "Failed to get paginated Posts." + e}],
        }
    }
}

const postGetPaginatedByAuthor = (authorId: number, skip: number = 0, take: number = 100): PostPayload => {
    if (!authorId || authorId < 0)
        return {
            errors: [{message: "Author Id must not be null and must be greater than zero."}]
        }

    if (skip < 0 || take < 0)
        return {
            errors: [{message: "Skip and Take parameters must be greater than zero."}]
        }

    try {
        return {
            errors: [],
            posts: postRepo.postGetPaginatedByAuthor(authorId, skip, take)
        }
    } catch (e) {
        return {
            errors: [{message: "Failed to get paginated Posts by author." + e}],
        }
    }
}

const postGetByPostId = (postId:number): PostPayload => {
    if (!postId || postId < 0)
        return {
            errors: [{message: "Post Id must not be null and must be greater than zero."}]
        }

    try {
        return {
            errors: [],
            post: postRepo.postGetByPostId(postId)
        }
    } catch (e) {
        return {
            errors: [{message: "Failed to get post by post id." + e}],
        }
    }
}

export const postService: PostService = {
    postInsert,
    postDelete,
    postGetPaginated,
    postGetPaginatedByAuthor,
    postGetByPostId
}
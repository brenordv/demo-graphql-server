import {Post} from "../models/post";
import {BooleanPayload} from "./boolean-interfaces";
import {BasePayloadInterface} from "./base-payload-interface";

export interface AddPostArgs {
    title: string,
    content: string,
    authorId: number
}

export interface InputAddPostArgs {
    input: {
        title: string,
        content: string
    }
}

export interface PostPayload extends BasePayloadInterface {
    posts?: Post[] | null,
    post?: Post | null
}

export interface PostService {
    postInsert(data: AddPostArgs): PostPayload,
    postDelete(postId: number): BooleanPayload,
    postGetPaginated(skip: number, take: number): PostPayload,
    postGetPaginatedByAuthor(authorId: number, skip: number, take: number): PostPayload,
    postGetByPostId(postId:number): PostPayload
}
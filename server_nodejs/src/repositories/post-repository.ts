import {getDatabase} from "./base";
import {Post} from "../models/post";
import {AddPostArgs} from "../interfaces/post-interfaces";
import {logger} from "../utils/log-utils";

const DELETE_POST = `DELETE FROM posts WHERE id = @postId`;
const INSERT_POST = `INSERT INTO posts (title, content, author_id) VALUES (@title, @content, @authorId)`;
const SELECT_POST = `SELECT
    id,
    title,
    content,
    author_id as authorId,
    strftime('%s', datetime(created_at, 'localtime')) as createdAt
FROM posts`;
const SELECT_POST_BY_POST_ID = `${SELECT_POST} WHERE id = @postId`;
const SELECT_POST_PAGINATED = `${SELECT_POST} ORDER BY created_at DESC LIMIT @take OFFSET @skip`;
const SELECT_POST_PAGINATED_BY_AUTHOR = `
${SELECT_POST} 
WHERE author_id = @authorId ORDER BY created_at DESC LIMIT @take OFFSET @skip`;

export const postInsert = (data: AddPostArgs): Post => {
    logger.verbose(`Inserting Post: [${data.authorId}] ${data.title}`);
    const db = getDatabase();
    const insert = db.prepare(INSERT_POST);
    const {lastInsertRowid} = insert.run(data);

    const insertedPost = {
        ...data,
        id: lastInsertRowid
    }

    return insertedPost as Post;
};

export const postGetPaginated = (skip: number, take: number): Post[] => {
    logger.verbose(`Getting paginated posts. Skip: ${skip} | Take: ${take}`);
    const db = getDatabase();
    const select = db.prepare(SELECT_POST_PAGINATED);
    const posts: Post[] = select.all({skip, take});
    posts.forEach(post => {
        post.createdAt = new Date((+post.createdAt)*1000);
    });
    return posts;
}

export const postGetPaginatedByAuthor = (authorId: number, skip: number, take: number): Post[] => {
    logger.verbose(`Getting paginated posts by author. Author Id: ${authorId} Skip: ${skip} | Take: ${take}`);
    const db = getDatabase();
    const select = db.prepare(SELECT_POST_PAGINATED_BY_AUTHOR);
    const posts: Post[] = select.all({authorId, skip, take});
    posts.forEach(post => {
        post.createdAt = new Date((+post.createdAt)*1000);
    });
    return posts;
}

export const postGetByPostId = (postId: number): Post | null=> {
    logger.verbose(`Getting post by its Id. Post Id: ${postId}`);
    const db = getDatabase();
    const select = db.prepare(SELECT_POST_BY_POST_ID);
    const post = select.get({postId});
    if (!post) return null;
    post.createdAt = new Date((+post.createdAt)*1000);
    return post;
}

export const postDelete = (postId: number): boolean => {
    logger.verbose(`Deleting post with id: ${postId}`);
    const post = postGetByPostId(postId);
    if (!post)
        throw new Error("No posts found with provided Id.");

    const db = getDatabase();
    const del = db.prepare(DELETE_POST);
    const {changes} = del.run({postId});
    return changes === 1;
}
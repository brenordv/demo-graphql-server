import {gql} from "apollo-server";

export const typeDefs = gql`
    type Query {
        posts(skip: Int, take: Int): PostsPayload
        me: UserPayload
        users(skip: Int, take: Int): UsersPayload
    }

    type Mutation {
        postCreate(input: PostInput!): PostPayload
        postDelete(postId: Int!): PostPayload
        signUp(input: SignUpInput!, bio: String!): AuthPayload
        signIn(username: String!, password: String!): AuthPayload
    }

    type Post {
        id: ID!
        title: String!
        content: String!
        createdAt: String!
        author: User!
    }

    type User {
        id: ID!
        name: String!
        email: String!
        username: String!
        profile: Profile
        posts: [Post!]!
    }

    type Profile {
        id: ID!
        bio: String!
        itsOwn: Boolean!
        user: User!
    }

    type Error {
        message: String!
    }

    type PostsPayload {
        errors: [Error]!
        posts: [Post!]!
    }

    type UserPayload {
        errors: [Error]!
        user: User
    }

    type UsersPayload {
        errors: [Error]!
        users: [User!]!
    }

    type PostPayload {
        errors: [Error]!
        post: Post
    }

    type AuthPayload {
        errors: [Error]!
        token: String
    }

    input PostInput {
        title: String!
        content: String!
    }

    input SignUpInput {
        name: String!
        username: String!
        email: String!
        password: String!
    }
`;
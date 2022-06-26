import {userService} from './services/user-service';
import {profileService} from './services/profile-service';
import {postService} from './services/post-service';
import {typeDefs} from "./schema";
import {ApolloServer} from "apollo-server";
import {Query} from "./resolvers/query";
import {Post} from "./resolvers/post";
import {User} from "./resolvers/user";
import {Profile} from "./resolvers/profile";
import {postResolvers} from "./resolvers/mutations/post-mutations";
import {authResolvers} from "./resolvers/mutations/auth-mutations";
import {getUserFromToken} from "./utils/jwt-utils";
import {logger} from "./utils/log-utils";

logger.info("Initializing GraphQl server...");
const Mutation = {
    ...authResolvers,
    ...postResolvers
}

const server = new ApolloServer({
    typeDefs,
    resolvers: {
        Query,
        Post,
        User,
        Profile,
        Mutation
    },
    context: ({req}) => {
        const token = req.headers.authorization;
        const userInfo = getUserFromToken(token);
        return {
            postService,
            profileService,
            userService,
            userInfo
        }
    }
});

logger.info("Starting GraphQl server...");
server.listen().then(({url}) => {
    logger.info(`Server ready on: ${url}`);
});
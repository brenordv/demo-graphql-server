import {PostService} from "./post-interfaces";
import {UserService} from "./user-interfaces";
import {ProfileService} from "./profile-interfaces";
import {UserInfo} from "../models/user";

export interface GraphqlContext {
    postService: PostService,
    userService: UserService,
    profileService: ProfileService,
    userInfo: UserInfo

}
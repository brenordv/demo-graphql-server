import {Profile} from "../models/profile";
import {BasePayloadInterface} from "./base-payload-interface";

export interface AddProfileArgs {
    userId: number,
    bio: string
}

export interface ProfilePayload extends BasePayloadInterface {
    profile?: Profile | null
}

export interface ProfileService {
    profileInsert(data: AddProfileArgs): ProfilePayload,
    profileUpdate(data: AddProfileArgs): ProfilePayload,
    profileGet(userId: number): ProfilePayload
}
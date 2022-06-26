import {BasePayloadInterface} from "./base-payload-interface";

export interface AuthPayload extends BasePayloadInterface {
    token?: string
}
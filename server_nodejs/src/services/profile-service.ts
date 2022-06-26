import {AddProfileArgs, ProfilePayload, ProfileService} from "../interfaces/profile-interfaces";
import * as profileRepo from '../repositories/profile-repository';

const validateAddProfileArgs = (data: AddProfileArgs): ProfilePayload | null => {
    if (!data)
        return {
            errors: [{message:"Input data cannot be null."}],
        }

    if (!data.userId || data.userId < 0)
        return {
            errors: [{message:"UserId must be provided and must be valid."}],
        }

    if (!data.bio)
        return {
            errors: [{message: "A bio must be provided."}],
        }

    return null;
}

const profileInsert = (data: AddProfileArgs): ProfilePayload => {
    const error = validateAddProfileArgs(data);
    if (error) return error;

    try {
        return {
            errors: [],
            profile: profileRepo.profileInsert(data)
        };
    }catch (e) {
        return {
            errors: [{message:"Failed to add Profile." + e}],
        }
    }
}

const profileUpdate = (data: AddProfileArgs): ProfilePayload => {
    const error = validateAddProfileArgs(data);
    if (error) return error;

    try {
        return {
            errors: [],
            profile: profileRepo.profileUpdate(data)
        };
    }catch (e) {
        return {
            errors: [{message:"Failed to update Profile." + e}],
        }
    }
}

const profileGet = (userId: number): ProfilePayload =>  {
    if (!userId || userId < 0)
        return {
            errors: [{message: "User Id cannot be null and must be a number greater than zero."}]
        }

    return {
        errors: [],
        profile: profileRepo.profileGet(userId)
    }
}

export const profileService: ProfileService = {
    profileInsert,
    profileUpdate,
    profileGet
}
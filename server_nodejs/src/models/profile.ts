export class Profile {
    constructor(
        public id: number,
        public bio: string,
        public userId: number,
        public createdAt: Date,
        public updatedAt: Date
    ) {
    }
}
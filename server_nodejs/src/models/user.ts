export class User {
    constructor(
        public id: number,
        public name: string,
        public username: string,
        public password: string,
        public email: string,
        public createdAt: Date,
        public updatedAt: Date,
    ) {
    }
}

export class UserInfo {
    constructor(
        public userId: number,
        public username: string
    ) {
    }
}
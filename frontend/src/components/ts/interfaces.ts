interface IUser {
    username: string;
    email: string;
    password?: string;
}

export interface IProfile {
    id: number;
    user: IUser;
    profile_img: string;
    bio: string;
}

export interface INotification {
    message: string;
    state: string;
    key: symbol; // this key will be used in a `keyed each block` to make it unique
}
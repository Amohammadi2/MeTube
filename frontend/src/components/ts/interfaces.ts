export interface IProfile {
    id: number;
    user: {
        username: string;
        email: string;
    };
    profile_img: string;
    bio: string;
}
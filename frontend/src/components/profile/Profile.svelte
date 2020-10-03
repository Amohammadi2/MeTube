<script lang="ts">
import { authToken } from "../ts/states";
import { APIRequest } from "../ts/api";
import type { IProfile } from "../ts/interfaces";

let profileImageUrl: string;
let bio: string;
let username: string;
let email: string;
let userId: number;

let login_username: string;
let login_password: string;

function login() {
    let login_url = `/users/get-auth-token/`;
    APIRequest.post(login_url, {
        username: login_username,
        password: login_password,
    })
    .then(response => {
        //localStorage.setItem("authToken", response.data.token);
        authToken.set(response.data.token);
        getProfile($authToken);
    })
    .catch(console.error);
}

function getProfile(auth_token) {
    let profile_url = `/users/get-profile/`;
    APIRequest.get(profile_url, {
        headers: {
            Authorization: "Token " + auth_token,
        }
    })
    .then(response => {
        let profile: IProfile = response.data;
        userId = profile.id;
        username = profile.user.username;
        email = profile.user.email;
        profileImageUrl = profile.profile_img;
    })
}

</script>


<template>
    {#if $authToken}
        <div class="flex-row">
            <img class="profile" src={profileImageUrl} alt="profile" />
            <h3>{username}</h3>
        </div>
        <div class="flex-row">
            <p>{email}</p>
            <p>{userId}</p>
        </div>
    {:else}
        <div class="box">
            <p style="margin-bottom: 10px">you haven't logged in</p>
            <form method="POST" on:submit|preventDefault>
                <div class="form-inputs">
                    <div class="form-input">
                        <input type="text" id="username" required autocomplete="off" bind:value={login_username}>
                        <label for="username" class="label">username</label>
                        <div class="magic-line"></div>
                    </div>
                    <div class="form-input">
                        <input type="password" id="password" required autocomplete="off" bind:value={login_password}>
                        <label for="password" class="label">password</label>
                        <div class="magic-line"></div>
                    </div>
                </div>
            </form>
            <button class="btn-green" on:click={login}>login</button>
            <button class="btn">register</button>
        </div>
    {/if}
</template>

<style lang="scss" src="./profile-style.scss"></style>
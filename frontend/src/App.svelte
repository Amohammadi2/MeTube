<script lang="ts">
import Sidebar from "./components/sidebar/Sidebar.svelte";
import { authToken } from "./components/ts/states";
import { Notifications } from "./components/ts/api";
import Notification from "./components/notification/Notification.svelte";
import type { INotification } from "./components/ts/interfaces";

import { onMount } from "svelte";

onMount(() => {
	new Notifications().error("notificatoins doesn't work");
})

// check if the user has logged in before or not
authToken.set(localStorage.getItem("authToken") || "");

let notifications_list: Array<INotification> = [];
Notifications._notifications.subscribe(value => {
	notifications_list = value;
	console.log (notifications_list);
});
</script>

<template>
	<div class="notification-box">
		{#each notifications_list as notification}
			<Notification
				message={notification.message}
				backgroundColor={new Notifications().states[notification.state]}
			/>
		{/each}
	</div>
	<Sidebar />
</template>

<style lang="scss">
	$small-width: 350px;

	.notification-box {
		position: fixed;
		right: 10px;
		bottom: 20px;
		width: $small-width;
		height: auto;
	}
</style>
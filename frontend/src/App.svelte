<script lang="ts">
import { flip } from "svelte/animate";
import Sidebar from "./components/sidebar/Sidebar.svelte";
import { authToken } from "./components/ts/states";
import { Notifier } from "./components/ts/api";
import Notification from "./components/notification/Notification.svelte";
import type { INotification } from "./components/ts/interfaces";

// check if the user has logged in before or not
authToken.set(localStorage.getItem("authToken") || "");

let notifications_list: Array<INotification> = [];
Notifier._notifications.subscribe(value => {
	notifications_list = value;
	console.log (notifications_list);
});
</script>

<template>
	<div class="notification-box">
		{#each notifications_list as notification (notification.key)}
			<div class="notification-wrapper" animate:flip={{duration: 150}}>
				<Notification
					message={notification.message}
					backgroundColor={new Notifier().states[notification.state]}
					on:click={event => Notifier.close(event, notification.key)}
				/>
			</div>
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
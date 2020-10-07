<script lang="ts">
import { fly } from "svelte/transition";
import { Notifier } from "../ts/api";

export let message: string;
// any rgb, hexadecimal value wich represents a color
export let backgroundColor: string;
</script>

<template>
    <div
        class="notification"
        style="background-color: {backgroundColor}"
        transition:fly="{{duration: 500, y: 300}}"
        on:click
    >
        {message}
    </div>
</template>

<style lang="scss" src="./notification-style.scss"></style>
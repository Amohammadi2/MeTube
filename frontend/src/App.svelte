<script lang="ts">
import Sidebar from "./components/sidebar/Sidebar.svelte";
import { authToken } from "./components/ts/states";

authToken.set(localStorage.getItem("authToken") || "");
</script>

<template>
	<Sidebar />
	hello world
</template>

<style lang="scss">

</style>
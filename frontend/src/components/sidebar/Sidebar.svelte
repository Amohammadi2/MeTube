<script lang="ts">
    import Profile from "../profile/Profile.svelte";
</script>
<style lang="scss" src="./sidebar-style.scss"></style>

<template>
    <div class="sidebar">
        <div class="sidebar-item">
            <span class="material-icons">person</span>
            <div class="floating-content">
                <Profile />
            </div>
        </div>
        <div class="sidebar-item">
            <span class="material-icons">add_alert</span>
        </div>
        <div class="sidebar-item">
            <span class="material-icons">settings</span>
        </div>
    </div>
</template>
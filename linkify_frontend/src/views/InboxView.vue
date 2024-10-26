<template>
    <div class="inbox-wrap flex flex-col justify-between pl-4 md:pl-0 pr-4 py-4">
        <FriendBar />
        <Chat />
    </div>
</template>

<script>
    import FriendBar from '@/components/FriendBar.vue'
    import Chat from '@/components/Chat.vue'

    export default {
        name: 'InboxView',
        components: {
            FriendBar,
            Chat,
        },
        setup() {

        }
    }
</script>


<style>
    .inbox-wrap {
        @apply w-full h-full overflow-hidden;
        height: 100vh;
    }
</style>
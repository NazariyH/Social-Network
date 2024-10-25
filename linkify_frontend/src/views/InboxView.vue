<template>
    <div class="inbox-wrap flex justify-between pr-4 py-8">
        <Chat />
        <FriendBar />
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
<template>
    <div class="w-full h-full rounded-3xl overflow-hidden relative ">
        <div class="h-full flex flex-col justify-between p-4">
            <div class="chat overflow-y-auto ">
                <Message />
                <Message />
                <Message />
                <Message />
                <Message />
                <Message />
                <Message />
                <Message />
            </div>
            <CreateMessage />
        </div>

        <img class="absolute w-full h-full top-0 left-0 object-cover -z-10" src="../assets/Decorations/chat_background.png" alt="">
    </div>
</template>

<script>
import CreateMessage from '@/components/CreateMessage.vue'
import Message from '@/components/Message.vue'

export default {
    name: 'Chat',
    components: {
        CreateMessage,
        Message,
    },
    setup() {

    }
}
</script>

<style>

</style>
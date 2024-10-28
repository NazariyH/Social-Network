<template>
    <div class="w-full h-auto text-white border-y py-2">
        <NotificationMessage />
        <NotificationMessage />
        <NotificationMessage />
        <NotificationMessage />
        <NotificationMessage />
        <NotificationMessage />
        <NotificationMessage />
        <NotificationMessage />
        <NotificationMessage />
        <NotificationMessage />
        <NotificationMessage />
    </div>
</template>


<script>
import NotificationMessage from '@/components/NotificationMessage.vue'


export default {
    name: 'Notification',
    components: {
        NotificationMessage,
    },
    setup() {

    }
}
</script>


<style>

</style>
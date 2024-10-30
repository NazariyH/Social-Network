<template>
    <div class="w-full h-auto text-white border-y py-2">
        <div v-if="noNotifications" class="text-black text-center">You have no notifications :)</div>
        <div v-else v-for="notification in notifications" :key="notification.id">
            <NotificationMessage :notification="notification" />
        </div>
    </div>
</template>

<script>
import NotificationMessage from '@/components/NotificationMessage.vue'
import { useNotificationStore } from '@/store/notification.js'
import { ref, onMounted } from 'vue'

export default {
    name: 'Notification',
    components: {
        NotificationMessage,
    },
    setup() {
        const notificationStore = useNotificationStore()
        const notifications = ref([])
        const noNotifications = ref(notificationStore.noNotifications)

        onMounted(async () => {
            await notificationStore.getNotificationList()
            noNotifications.value = notificationStore.noNotifications

            if (noNotifications.value)
                return

            // Access the notifications property directly
            if (Array.isArray(notificationStore.notificationList.notifications)) {
                notifications.value = [...notificationStore.notificationList.notifications]
            } else {
                console.error('Notification list is not an array:', notificationStore.notificationList.notifications)
            }
        });


        return { notifications, noNotifications }
    }
}
</script>

<style></style>

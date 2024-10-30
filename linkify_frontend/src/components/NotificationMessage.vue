<template>
    <div v-if="noNotifications" class="text-black text-center">You have no notifications :)</div>
    <div v-else :class="['w-full', 'flex', 'justify-between', 'items-center', 'my-2', 'py-2', 
    'px-4', 'rounded-2xl', 'transition', 'ease-linear', 'duration-100', randomColor]">
        <span class="break-words w-3/4">{{ notification.title }}</span>

        <button @click="removeNotification($event, notification.id)" class="text-xl">
            <i class="fa-solid fa-circle-xmark"></i>
        </button>
    </div>
</template>


<script>
import { useColorsStore } from '@/store/colors'
import { useNotificationStore } from '@/store/notification'
import { ref } from 'vue'

export default {
    name: 'NotificationMessage',
    props: ['notification'],
    setup() {
        const colorsStore = useColorsStore()
        const randomColor = ref(colorsStore.getRandomColor())
        const notificationStore = useNotificationStore()

        const noNotifications = ref(notificationStore.noNotifications)


        function removeNotification(even, id) {
            notificationStore.deleteNotification(id).then(() => noNotifications.value = notificationStore.noNotifications)

            const notification = event.target.parentElement.parentElement
            notification.classList.add('translate-x-full')

            
            setTimeout(() => notification.remove(), 100)
        }

        return {
            randomColor,
            noNotifications,
            removeNotification
        }
    }
}
</script>
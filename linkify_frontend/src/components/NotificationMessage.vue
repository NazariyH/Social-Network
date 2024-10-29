<template>
    <div :class="['w-full', 'flex', 'justify-between', 'items-center', 'my-2', 'py-2', 
    'px-4', 'rounded-2xl', 'transition', 'ease-linear', 'duration-100', randomColor]">
        <div class="flex items-center">
            <div class="bg-white p-2 rounded-2xl me-2">
                <div class="size-6 rounded-full loading"></div>
            </div>

            <span><router-link to="empty">@Nazariy</router-link> started folowing you</span>
        </div>

        <button @click="removeNotification($event)" class="text-xl">
            <i class="fa-solid fa-circle-xmark"></i>
        </button>
    </div>
</template>


<script>
import { useColorsStore } from '@/stores/colors'
import { ref } from 'vue'

export default {
    name: 'NotificationMessage',
    setup() {
        const colorsStore = useColorsStore()
        const randomColor = ref(colorsStore.getRandomColor())


        function removeNotification(event) {
            const notification = event.target.parentElement.parentElement
            notification.classList.add('translate-x-full')

            setTimeout(() => notification.remove(), 100)
        }

        return {
            randomColor,
            removeNotification
        }
    }
}
</script>
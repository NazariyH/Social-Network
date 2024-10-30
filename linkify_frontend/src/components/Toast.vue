<template>
    <div 
        id="toast"
        v-if="true" 
        class="fixed bottom-4 right-0 translate-x-full bg-emerald-700 opacity-20 transition ease-in-out delay-300 duration-300 py-2 px-4 rounded-xl text-white" 
        :class="toastStore.classes">
        <span>{{ toastStore.message }}</span>
    </div>
</template>

<script>
import { useToastStore } from '@/store/toast'

export default {
    name: 'Toast',
    setup() {
        const toastStore = useToastStore()

        return { toastStore }
    }
}
</script>


<style>
    #toast.active {
        @apply -translate-x-4 bg-emerald-700 opacity-100;
    }
</style>
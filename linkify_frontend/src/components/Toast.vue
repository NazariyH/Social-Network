<template>
    <div 
        id="toast"
        v-if="true" 

        class="fixed bottom-4 -right-full transition ease-in-out delay-500 duration-300 py-2 px-4 rounded-xl text-white" 
        :class="toastStore.classes"
    >
        {{ toastStore.message }}
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
        @apply right-4 bg-emerald-700;
    }
</style>
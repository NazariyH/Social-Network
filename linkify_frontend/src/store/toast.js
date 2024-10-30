import { defineStore } from 'pinia'


export const useToastStore = defineStore({
    id: 'toast',
    state: () => ({
        ms: 0,
        message: '',
        classes: '',
        isVisible: false
    }),

    actions: {
        showToast(ms, message, classes) {
            this.ms = parseInt(ms)
            this.message = message
            this.classes = classes
            this.isVisible = true

            setTimeout(() => {
                this.classes += ' active'
            }, 10)


            setTimeout(() => {
                this.classes = this.classes.replace('active', '')

            }, this.ms - 1000)


            setTimeout(() => {
                this.isVisible = false
            }, this.ms)
        }
    }
})
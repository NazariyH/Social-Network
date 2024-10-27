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
                this.classes += ' -translate-x-32'
            }, 10)


            setTimeout(() => {
                this.classes = this.classes.replace('-translate-x-32', '')

            }, this.ms - 500)


            setTimeout(() => {
                this.isVisible = false
            }, this.ms)
        }
    }
})
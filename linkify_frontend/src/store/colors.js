import { defineStore } from 'pinia'


export const useColorsStore = defineStore({
    id: 'colors',
    
    state: () => ({
        colors: [
            "bg-red-500",
            "bg-orange-500",
            "bg-yellow-500",
            "bg-green-500",
            "bg-blue-500",
            "bg-indigo-500",
            "bg-purple-500",
            "bg-pink-500",
        ]
    }),

    actions: {
        getRandomColor() {
            const randomIndex = Math.floor(Math.random() * this.colors.length)
            return this.colors[randomIndex]
        }
    }
})
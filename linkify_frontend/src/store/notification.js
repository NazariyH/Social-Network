import { defineStore } from 'pinia'
import axios from 'axios'

export const useNotificationStore = defineStore({
    id: 'Notification',

    state: () => ({
        notificationList: []
    }),

    actions: {
        async getNotificationList() {
            const url = '/api/notification/get/'
            const user_access_token = localStorage.getItem('user.access')

            try {
                const response = await axios.get(url, {
                    headers: {
                        'Authorization': `Bearer ${user_access_token}`
                    }
                })

                if (response) {
                    this.notificationList = response.data
                }
            } catch (error) {
                console.log('Something went wrong', error)
            }
        },

        async deleteNotification(id) {
            const url = `/api/notification/${id}/delete/`
            const user_access_token = localStorage.getItem('user.access')

            try {
                const response = await axios.delete(url, {
                    headers: {
                        'Authorization': `Bearer ${user_access_token}`
                    }
                })


                if (response) {
                    this.notificationList = response.data
                }
            } catch (error) {
                console.log('Something went wrong', error)
            }
        }
    }
})
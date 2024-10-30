import { defineStore } from 'pinia'
import axios from 'axios'

export const useNotificationStore = defineStore({
    id: 'Notification',

    state: () => ({
        notificationList: [],
        noNotifications: true,
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

                    if (this.notificationList.notifications.length !== 0)
                        this.noNotifications = false
                    else
                        this.noNotifications = true
                }
            } catch (error) {
                this.noNotifications = true

                if (error.status !== 404)
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

                    if (this.notificationList.notifications.length !== 0)
                        this.noNotifications = false
                    else
                        this.noNotifications = true
                }
            } catch (error) {
                this.noNotifications = true
                
                if (error.status !== 404)
                    console.log('Something went wrong', error)
            }
        }
    }
})
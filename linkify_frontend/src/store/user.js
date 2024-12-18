import { defineStore } from 'pinia'
import axios from 'axios'


export const useUserStore = defineStore({
    id: 'user',

    state: () => ({
        user: {
            isAuthenticated: false,
            id: null,
            name: null,
            email: null,
            access: null,
            refresh: null,
        }
    }),

    actions: {
        initStore() {
            if (localStorage.getItem('user.access')) {
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.id = localStorage.getItem('user.id')
                this.user.name = localStorage.getItem('user.name')
                this.user.email = localStorage.getItem('user.email')
                this.user.isAuthenticated = true

                this.refreshToken()
            }
        },


        setToken(data) {
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)
        },


        removeToken() {
            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = null
            this.user.id = false
            this.user.name = false
            this.user.email = false

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.email', '')
        },


        setUserInfo(user) {
            this.user.id = user.id
            this.user.name = user.name
            this.user.email = user.email

            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.name', this.user.name)
            localStorage.setItem('user.email', this.user.email)
        },


        async refreshToken() {
            const url = '/api/refresh/'

            try {
                const response = await axios.post(url, {
                    refresh: this.user.refresh
                })

                if (response) {
                    this.user.access = response.data.access

                    localStorage.setItem('user.access', this.user.access)

                    axios.defaults.headers.common["Authorization"] = `Bearer ${response.data.access}`
                }
            } catch (error) {
                console.log('fasfasdas')
                console.log(error)

                this.removeToken()
            }
        }
    }
})
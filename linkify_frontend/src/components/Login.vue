<template>
    <form id="login" @submit.prevent="submitForm">
        <div class="input-wrap">
            <label for="email">Email</label>
            <input id="email" type="email" v-model="submitFormData.email" class="input">
        </div>

        <div class="input-wrap">
            <label for="password">Password</label>

            <div class="flex">
                <input id="password" :type="show_password ? 'text' : 'password'" v-model="submitFormData.password"
                    class="input">
                <button @click.prevent="toggleShowPassword">
                    <i v-if="show_password" class="fa-solid fa-eye"></i>
                    <i v-else class="fa-solid fa-eye-slash"></i>
                </button>
            </div>

            <router-link class="96 text-blue-700 text-sm">Forgot password?</router-link>
        </div>

        <button type="submit" class="btn btn-submit">Log in</button>

        <template v-if="errors.length > 0">
            <div class="bg-red-500 text-white rounded-2xl px-4 py-2 mt-4">
                <ul>
                    <li v-for="error in errors" :key="error">{{ error }}</li>
                </ul>
            </div>
        </template>
    </form>
</template>


<script>
import { useToggleFunction } from '@/composables/useTogglePassword'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'
import axios from 'axios'

export default {
    name: 'Login',
    setup() {
        const { show_password, toggleShowPassword } = useToggleFunction()
        const { setToken } = useUserStore()
        const toastStore = useToastStore()

        return { show_password, toggleShowPassword, setToken, toastStore }
    },
    data() {
        return {
            submitFormData: {
                email: '',
                password: '',
            },
            errors: [],
        }
    },
    methods: {
        async submitForm() {
            this.errors = []

            if (this.errors.length === 0) {
                try {
                    const response = await axios.post('/api/login/', this.submitFormData)
                    if (response) {
                        this.setToken(response.data)

                        axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access || response.data.token}`


                        this.toastStore.showToast(5000, 'The user is loged in', 'bg-emerald-500')

                        this.submitFormData.email = ''
                        this.submitFormData.password = ''

                        this.$router.push({ name: 'home' })
                    }
                } catch (error) {
                    if (error.response && error.response.data && error.response.data.detail) {
                        this.errors.push(error.response.data.detail)
                    } else {
                        this.errors.push('An error occurred. Please try fagain.')
                    }
                }
            }
        }
    }
}
</script>

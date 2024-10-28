<template>
    <form id="signup" class="hidden" @submit.prevent="submitForm">
        <div class="input-wrap">
            <label for="name">Name</label>
            <input id="name" type="text" class="input" v-model="form.name" required>
        </div>

        <div class="input-wrap">
            <label for="email">Email</label>
            <input id="email" type="email" class="input" v-model="form.email" required>
        </div>

        <div class="input-wrap">
            <label for="password">Password</label>

            <div class="flex">
                <input id="password" :type="show_password ? 'text' : 'password'" v-model="form.password1" class="input"
                    required>
                <button @click.prevent="toggleShowPassword">
                    <i v-if="show_password" class="fa-solid fa-eye"></i>
                    <i v-else class="fa-solid fa-eye-slash"></i>
                </button>
            </div>
        </div>

        <div class="input-wrap">
            <label for="confirm-password">Password</label>

            <div class="flex">
                <input id="confirm-password" :type="show_password ? 'text' : 'password'" v-model="form.password2"
                    class="input" required>
                <button @click.prevent="toggleShowPassword">
                    <i v-if="show_password" class="fa-solid fa-eye"></i>
                    <i v-else class="fa-solid fa-eye-slash"></i>
                </button>
            </div>
        </div>

        <button type="submit" class="btn btn-submit">Sign up</button>

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
import { useToggleAuthTabFunction } from '@/composables/useToggleAuthTab'
import { useToastStore } from '@/stores/toast';
import axios from 'axios'

export default {
    name: 'Signup',
    setup() {
        const { show_password, toggleShowPassword } = useToggleFunction()
        const { isLoginActive, switchLogin } = useToggleAuthTabFunction()
        const toastStore = useToastStore()

        return { show_password, toggleShowPassword, toastStore, switchLogin }
    },
    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: '',
            },
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors = []

            if (this.errors.length === 0) {
                try {
                    const response = await axios.post('/api/signup/', this.form)

                    if (response) {
                        this.toastStore.showToast(5000, 'The user is registered. Please log in', 'bg-emerald-500')

                        // Clear form fields
                        this.form.email = ''
                        this.form.name = ''
                        this.form.password1 = ''
                        this.form.password2 = ''

                        this.switchLogin()
                    }

                } catch (error) {
                    if (error.response && error.response.data && error.response.data.message) {
                        this.errors.push(error.response.data.message)
                    } else {
                        this.errors.push('An error occurred. Please try again.')
                    }
                }
            }
        }
    }
}
</script>

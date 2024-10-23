<template>
    <form id="login">
        <div class="input-wrap">
            <label for="name">Name</label>
            <input id="name" type="text" class="input">
        </div>

        <div class="input-wrap">
            <label for="password">Password</label>

            <div class="flex">
                <input id="password" :type="show_password ? 'text' : 'password'" class="input">
                <button @click.prevent="toggleShowPassword">
                    <i v-if="show_password" class="fa-solid fa-eye"></i>
                    <i v-else class="fa-solid fa-eye-slash"></i>
                </button>
            </div>

            <router-link class="96 text-blue-700 text-sm">Forgot password?</router-link>
        </div>

        <button type="submiy" class="btn w-96 h-10">Log in</button>
    </form>
</template>


<script>
import { useToggleFunction } from '@/composables/useTogglePassword'

export default {
    name: 'Login',
    setup() {
        const { show_password, toggleShowPassword } = useToggleFunction()

        return { show_password, toggleShowPassword }
    }
}
</script>

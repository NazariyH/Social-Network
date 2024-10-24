<template>
    <form id="signup" class="hidden">
        <div class="input-wrap">
            <label for="name">Name</label>
            <input id="name" type="text" class="input">
        </div>

        <div class="input-wrap">
            <label for="email">Email</label>
            <input id="email" type="email" class="input">
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
        </div>

        <button type="submiy" class="btn btn-submit">Sign up</button>
    </form>
</template>


<script>
import { useToggleFunction } from '@/composables/useTogglePassword'

export default {
    name: 'Signup',
    setup() {
        const { show_password, toggleShowPassword } = useToggleFunction()

        return { show_password, toggleShowPassword }
    }
}
</script>

<template>
    <div id="authorization-wrap" class="w-full h-full flex flex-col items-center justify-center relative">
        <div class="bg-white p-8 rounded-3xl">
            <div class="font-bold text-gray-500 mb-8">
                <span @click="switchLogin" id="login-tab" class="cursor-pointer me-8 auth-tab-active">
                    Login
                </span>
                <span @click="switchSignup" id="signup-tab" class="cursor-pointer">
                    Signup
                </span>
            </div>

            <Login />
            <Signup />
        </div>

        <img src="../assets/Decorations/auth_decoration.png" class="absolute w-full h-full object-cover -z-10" alt="">
    </div>
</template>


<script>
import { useToggleAuthTabFunction } from '@/composables/useToggleAuthTab'
import Login from '@/components/Login.vue'
import Signup from '@/components/Signup.vue'

export default {
    name: 'AuthenticationView',
    components: {
        Login,
        Signup,
    },
    setup() {
        const { switchLogin, switchSignup } = useToggleAuthTabFunction()

        return { switchLogin, switchSignup}
    }
}
</script>


<style>
#authorization-wrap {
    height: 100vh;
}

.input {
    @apply block w-64 sm:w-96 h-10 bg-gray-100 mt-2 px-4 rounded-2xl;
}

.input-wrap {
    @apply mb-8;
}

#password,
#confirm-password {
    @apply w-48 sm:w-80 rounded-e-none;
}

#password + button,
#confirm-password + button {
    @apply flex justify-center items-center mt-2 w-16 h-10 bg-gray-100 rounded-e-2xl;
}

label {
    @apply font-bold;
}

.auth-tab-active {
    @apply text-black border-b-2 border-black pb-1;
}

.btn-submit {
    @apply w-64 sm:w-96 h-10;
}
</style>
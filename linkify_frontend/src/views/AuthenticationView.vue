<template>
    <div id="authorization-wrap" class="w-full h-full flex flex-col items-center justify-center relative">
        <div class="bg-white p-8 rounded-3xl">
            <div class="font-bold text-gray-500 mb-8">
                <span @click="switchLogin" :class="{ 'cursor-pointer me-8': true, 'auth-tab-active': isLoginActive }">
                    Login
                </span>
                <span @click="switchSignup" :class="{ 'cursor-pointer': true, 'auth-tab-active': !isLoginActive }">
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
import { useToggleFunction } from '@/composables/useTogglePassword'
import { ref } from 'vue'
import Login from '@/components/Login.vue'
import Signup from '@/components/Signup.vue'

export default {
    name: 'AuthenticationView',
    components: {
        Login,
        Signup,
    },
    setup() {
        const isLoginActive = ref(true)


        function switchLogin(event) {
            isLoginActive.value = true

            const loginBlock = document.getElementById('login')
            if (loginBlock.classList.contains('hidden'))
                loginBlock.classList.remove('hidden')

            const signupBlock = document.getElementById('signup')
            if (!signupBlock.classList.contains('hidden'))
                signupBlock.classList.add('hidden')
        }


        function switchSignup(event) {
            isLoginActive.value = false

            const loginBlock = document.getElementById('login')
            if (!loginBlock.classList.contains('hidden'))
                loginBlock.classList.add('hidden')

            const signupBlock = document.getElementById('signup')
            if (signupBlock.classList.contains('hidden'))
                signupBlock.classList.remove('hidden')
        }

        return { isLoginActive, switchLogin, switchSignup }
    }
}
</script>


<style>
#authorization-wrap {
    height: 100vh;
}

.input {
    @apply block w-96 h-10 bg-gray-100 mt-2 px-4 rounded-2xl;
}

.input-wrap {
    @apply mb-8;
}

#password,
#confirm-password {
    @apply w-80 rounded-e-none;
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
</style>
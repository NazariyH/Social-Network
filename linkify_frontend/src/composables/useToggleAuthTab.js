import { ref } from 'vue'

export function useToggleAuthTabFunction() {

    function switchLogin() {
        const loginTab = document.getElementById('login-tab')
        const signupTab = document.getElementById('signup-tab')

        if (!loginTab.classList.contains('auth-tab-active')) {
            if (signupTab.classList.contains('auth-tab-active'))
                signupTab.classList.remove('auth-tab-active')
            loginTab.classList.add('auth-tab-active')
        }

        const loginBlock = document.getElementById('login')
        if (loginBlock.classList.contains('hidden'))
            loginBlock.classList.remove('hidden')

        const signupBlock = document.getElementById('signup')
        if (!signupBlock.classList.contains('hidden'))
            signupBlock.classList.add('hidden')
    }


    function switchSignup() {
        const loginTab = document.getElementById('login-tab')
        const signupTab = document.getElementById('signup-tab')

        if (!signupTab.classList.contains('auth-tab-active')) {
            if (loginTab.classList.contains('auth-tab-active'))
                loginTab.classList.remove('auth-tab-active')
            signupTab.classList.add('auth-tab-active')
        }

        const loginBlock = document.getElementById('login')
        if (!loginBlock.classList.contains('hidden'))
            loginBlock.classList.add('hidden')

        const signupBlock = document.getElementById('signup')
        if (signupBlock.classList.contains('hidden'))
            signupBlock.classList.remove('hidden')
    }


    return { switchLogin, switchSignup }
}
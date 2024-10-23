import { ref } from 'vue'

export function useToggleFunction() {
    let show_password = ref(false)
    

    function toggleShowPassword() {
        show_password.value = !show_password.value
    }
    
    return { show_password, toggleShowPassword }
}

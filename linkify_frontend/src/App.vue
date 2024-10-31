<template>
	<main class="w-full flex justify-between">
		<Navbar />

		<RouterView />

		<Toast />
	</main>
</template>


<script>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import Toast from '@/components/Toast.vue'

import { useUserStore } from '@/store/user'
import axios from 'axios'


export default {
	components: {
		Navbar,
		Toast
	},
	setup() {
		const userStore = useUserStore()

		return { userStore }
	},
	beforeCreate() {
		this.userStore.initStore()

		const token = this.userStore.user.access

		if(token) {
			axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
		} else {
			axios.defaults.headers.common['Authorization'] = ''
		}
	}
}
</script>
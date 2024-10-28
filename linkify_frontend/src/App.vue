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

export default {
	components: {
		Navbar,
		Toast
	},
	setup() {

	}
}
</script>
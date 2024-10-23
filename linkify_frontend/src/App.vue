<template>
	<main class="w-full flex justify-between">
		<Navbar />

		<RouterView />
	</main>
</template>


<script>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '@/components/Navbar.vue'

export default {
	components: {
		Navbar,
	},
	setup() {

	}
}
</script>
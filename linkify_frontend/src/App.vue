<template>
	<main class="w-full flex justify-between">
		<Navbar />


		<div class="w-full pe-4">
			<div class="w-full flex justify-between py-8">
				<h1 class="text-xl font-bold">Feeds</h1>

				<div>
					<button class="ml-4 font-bold text-sm text-gray-500">Recents</button>
					<button class="ml-4 font-bold text-sm text-gray-500 sort-button-active">Friends</button>
					<button class="ml-4 font-bold text-sm text-gray-500">Popular</button>
				</div>
			</div>


			<div>
				<div class="w-full h-72 mb-8 bg-red-500 rounded-3xl"></div>
				<div class="w-full h-52 mb-8 bg-yellow-500 rounded-3xl"></div>
				<div class="w-full h-64 mb-8 bg-emerald-500 rounded-3xl"></div>
				<div class="w-full h-72 mb-8 bg-red-500 rounded-3xl"></div>
				<div class="w-full h-52 mb-8 bg-yellow-500 rounded-3xl"></div>
				<div class="w-full h-64 mb-8 bg-emerald-500 rounded-3xl"></div>
				<div class="w-full h-72 mb-8 bg-red-500 rounded-3xl"></div>
				<div class="w-full h-52 mb-8 bg-yellow-500 rounded-3xl"></div>
				<div class="w-full h-64 mb-8 bg-emerald-500 rounded-3xl"></div>
				<div class="w-full h-72 mb-8 bg-red-500 rounded-3xl"></div>
				<div class="w-full h-52 mb-8 bg-yellow-500 rounded-3xl"></div>
				<div class="w-full h-64 mb-8 bg-emerald-500 rounded-3xl"></div>
			</div>
		</div>

		<RecomendationBar />
	</main>

	<RouterView />
</template>


<script>
	import { RouterLink, RouterView } from 'vue-router'
	import Navbar from '@/components/Navbar.vue'
	import RecomendationBar from '@/components/RecomendationBar.vue'

	export default {
		components: {
			Navbar,
			RecomendationBar,
		},
		setup() {

		}
	}
</script>
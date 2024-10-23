<template>
	<div class="w-full px-4">
		<div class="w-full flex justify-between py-8">
			<h1 class="text-xl font-bold">Feeds</h1>

			<div>
				<button class="ml-4 font-bold text-sm text-gray-500">Recents</button>
				<button class="ml-4 font-bold text-sm text-gray-500 sort-button-active">Friends</button>
				<button class="ml-4 font-bold text-sm text-gray-500">Popular</button>
			</div>
		</div>


		<div>
			<div class="w-full h-72 mb-8 bg-purple-400 rounded-3xl"></div>
			<div class="w-full h-64 mb-8 bg-emerald-500 rounded-3xl"></div>
			<div class="w-full h-52 mb-8 bg-rose-400 rounded-3xl"></div>
			<div class="w-full h-72 mb-8 bg-cyan-500 rounded-3xl"></div>
			<div class="w-full h-52 mb-8 bg-pink-500 rounded-3xl"></div>
			<div class="w-full h-64 mb-8 bg-amber-500 rounded-3xl"></div>
		</div>
	</div>

	<RecomendationBar />
</template>


<script>
import RecomendationBar from '@/components/RecomendationBar.vue'

export default {
	name: 'HomeView',
	components: {
		RecomendationBar,
	},
	setup() {

	}
}
</script>


<style>
.sort-button-active {
	@apply text-black;
}

.side-block {
	height: 100vh;
}
</style>
<template>
	<div class="w-full min-w-64 min-h-full px-2 md:px-4 overflow-y-hidden">
		<CreatePost />

		<div class="w-full flex justify-between py-8">
			<h1 class="text-xl font-bold">Feeds</h1>

			<div>
				<button class="ml-4 font-bold text-sm text-gray-500">Recents</button>
				<button class="ml-4 font-bold text-sm text-gray-500 sort-button-active">Friends</button>
				<button class="ml-4 font-bold text-sm text-gray-500">Popular</button>
			</div>
		</div>


		<div>
			<Post />
			<Post />
			<Post />
		</div>
	</div>

	<RecomendationBar />
</template>


<script>
import RecomendationBar from '@/components/RecomendationBar.vue'
import CreatePost from '@/components/CreatePost.vue'
import Post from '@/components/Post.vue'

export default {
	name: 'HomeView',
	components: {
		RecomendationBar,
		CreatePost,
		Post,
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
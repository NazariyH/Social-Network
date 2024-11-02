<template>
	<div class="w-full flex">
		<div class="w-full min-w-64 min-h-full overflow-y-hidden">
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
				<Post v-for="post in post_list" :post="post" :key="post.id" />
			</div>
		</div>

		<RecomendationBar />
	</div>
</template>


<script>
import RecomendationBar from '@/components/RecomendationBar.vue'
import CreatePost from '@/components/CreatePost.vue'
import Post from '@/components/Post.vue'

import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
	name: 'HomeView',
	components: {
		RecomendationBar,
		CreatePost,
		Post,
	},
	setup() {
		const post_list = ref([])


		async function getPostList() {
			const url = '/api/posts/'

			try {
				const response = await axios.get(url)

				if (!response)
					return

				post_list.value = response.data.post_list
			} catch (error) {
				console.log('Something went wrong', error)
			}
		}

		onMounted(() => {
			getPostList()
		})

		return { post_list }
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
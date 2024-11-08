<template>
    <div class="post-detail-wrap">
        <div v-if="post" class="my-8 mx-4 md:ms-0">
            <Post :post="post" />
        </div>
        <div v-else class="w-full h-full flex justify-center items-center">
            <span class="spiner"></span>
        </div>
    </div>
</template>


<script>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'

import Post from '@/components/Post.vue'

export default {
    name: 'PostDetailView',
    components: {
        Post
    },
    setup() {
        const route = useRoute()
        const post = ref(null)
        const postId = route.params.id



        async function getPost(postId) {
            if (!postId) return

            try {
                const url = `/api/posts/${postId}/detail/`
                const response = await axios.get(url)

                post.value = response.data
            } catch (error) {
                console.log('Oops. Something went wrong :(', error)
            }
        }


        onMounted(() => {
            getPost(postId)
        })

        return { post }
    }
}
</script>


<style>
.post-detail-wrap {
    width: 100vw;
    height: 100vh;
}
</style>
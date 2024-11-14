<template>
    <div class="h-auto w-full md:w-profile-view text-black p-4 md:pl-0">
        <ProfileInfo :profile="profile" />

        <div class="mt-4">
            <Post v-for="post in posts" :key="post.id" :post="post" />
        </div>
    </div>
</template>


<script>
import ProfileInfo from '@/components/ProfileInfo.vue'
import Post from '@/components/Post.vue'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

export default {
    name: 'ProfileView',
    components: {
        ProfileInfo,
        Post,
    },
    setup() {
        const route = useRoute()

        const profile = ref({})


        onMounted(() => {
            fetchProfileInfo()
        })


        async function fetchProfileInfo() {
            const userId = route.params.id
            const url = `/api/profile/${userId}/`

            try {
                const response = await axios.get(url)

                console.log(response.data.profile)
                profile.value = response.data.profile
            } catch (error) {
                console.log('Oops. Something went wrong :(', error)
            }

        }

        return { profile }
    }
}
</script>

<template>
    <div class="w-full h-auto break-words">
        <div class="w-full h-14 py-2 px-4 flex justify-between items-center rounded-3xl bg-gray-50 pl-12 md:ps-4">
            <div class="flex items-center h-full">
                <h4 class="font-bold">Friends: 
                    <span v-if="profile.friends_count">{{ profile.friends_count }}</span>
                    <span v-else>0</span>
                </h4>

                <button v-if="!profile.is_current_user" class="btn px-4 ms-4 h-full">Add to friend</button>
            </div>

            <button v-if="profile.is_current_user" class="btn px-4 h-full">Log out</button>
        </div>

        <div class="profile-block-info w-full mt-4 flex flex-col lg:flex-row">
            <div class="profile-block-info p-4 w-full lg:w-1/2 lg:me-2 flex rounded-3xl bg-gray-50 mb-4 lg:mb-0">
                <div class="size-64 rounded-full overflow-hidden loading mr-4">
                    <img v-if="profile.avatar" class="size-full object-cover" :src="profile.avatar" alt="">
                </div>

                <div class="h-full flex flex-col">
                    <div class="mb-4">
                        <h4 v-if="profile.email" class="gray-text mb-4">{{ profile.email }}</h4>
                        <h1 v-if="profile.name" class="font-bold text-3xl">{{ profile.name }}</h1>
                    </div>

                    <div>
                        <div class="flex mb-4">
                            <div v-if="profile.age" class="me-4">
                                <h3 class="gray-text mb-2">Age</h3>
                                <h1 class="text-2xl font-bold">{{ profile.age }}</h1>
                            </div>

                            <div v-if="profile.origin">
                                <h3 class="gray-text mb-2">Origin</h3>
                                <h1 class="text-2xl font-bold">{{ profile.origin }}</h1>
                            </div>
                        </div>

                        <div v-if="profile.social_networks" class="flex">
                            <a v-for="social_network in profile.social_networks" 
                            :key="social_network.id" 
                            :href="social_network.link">
                                <img class="size-8 me-4 hover:scale-125 hover:opacity-80 transition ease-in-out duration-200"
                                    :src="social_network.icon" alt="">
                            </a>
                        </div>
                    </div>
                </div>
            </div>


            <div class="profile-block-info p-4 w-full lg:w-1/2 lg:ms-2 rounded-3xl bg-gray-50 overflow-y-auto">
                <div v-if="profile.bio" class="mb-4">
                    <h1 class="gray-text font-bold mb-2 font-2xl">About me</h1>
                    <p>{{ profile.bio }}</p>
                </div>

                <div v-if="profile.hashtags">
                    <h1 class="gray-text font-bold mb-2 font-2xl">My hashtags</h1>
                    <div class="flex flex-wrap">
                        <span v-for="hashtag in profile.hashtags" 
                        :class="['hashtag-pillow', generateColor()]"
                        :key="hashtag.id">{{ hashtag.name }}</span>
                    </div>
                </div>

                <div v-if="!profile.bio && !profile.hashtags" class="flex justify-center items-center w-full h-full">
                    <p class="gray-text font-bold text-2xl">No info</p>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import { useColorsStore } from '@/store/colors'
import { ref } from 'vue'

export default {
    name: 'ProfileInfo',
    props: ['profile'],
    setup() {
        const colorsStore = useColorsStore()
        const randomColor = colorsStore.getRandomColor()

        function generateColor() {
            return colorsStore.getRandomColor()
        }

        return { colorsStore, generateColor }
    }
}
</script>

<style>
.profile-block-info {
    /* min-height: 100px; */
}

.gray-text {
    @apply text-gray-400;
}

.hashtag-pillow {
    @apply px-4 py-2 text-sm text-white font-bold rounded-2xl me-4 my-2 hover:opacity-70 transition ease-in-out duration-200;
}
</style>
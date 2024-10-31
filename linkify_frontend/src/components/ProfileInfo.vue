<template>
    <div class="w-full h-auto break-words">
        <div class="w-full h-14 py-2 px-4 flex justify-between items-center rounded-3xl bg-gray-50 pl-12 md:ps-4">
            <div>
                <span class="font-bold">Friends: {{ profile.friendsCount }}</span>

                <button v-if="!profile.isCurrentUser" class="btn px-4 ms-4 h-full">Add to friend</button>
            </div>

            <button v-if="profile.isCurrentUser" class="btn px-4 ms-4 h-full">Log out</button>
        </div>

        <div class="profile-block-info w-full mt-4 flex flex-col lg:flex-row">
            <div class="profile-block-info p-4 w-full lg:w-1/2 lg:me-2 flex rounded-3xl bg-gray-50 mb-4 lg:mb-0">
                <div class="size-64 rounded-full overflow-hidden loading mr-4">
                    <img class="size-full object-cover" :src="profile.profileImage" alt="">
                </div>

                <div class="h-full flex flex-col">
                    <div class="mb-4">
                        <h4 class="gray-text mb-4">{{ profile.email }}</h4>
                        <h1 class="font-bold text-3xl">{{ profile.name }}</h1>
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

                        <div class="flex">
                            <a v-for="socialMedia in profile.socialMedias" :href="socialMedia[1]">
                                <img class="size-8 me-4 hover:scale-125 transition ease-in-out duration-200"
                                    :src="`/src/assets/social_media/${socialMedia[0]}.png`" alt="">
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="profile-block-info p-4 w-full lg:w-1/2 lg:ms-2 rounded-3xl bg-gray-50 overflow-y-auto">
                <div class="mb-4">
                    <h1 class="gray-text font-bold mb-2 font-2xl">About me</h1>
                    <p>{{ profile.bio }}</p>
                </div>

                <div>
                    <h1 class="gray-text font-bold mb-2 font-2xl">My goals</h1>
                    <div class="flex flex-wrap">
                        <span v-for="goal in profile.goals" :class="['goal-pillow', generateColor()]">{{ goal
                            }}</span>
                    </div>
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

.goal-pillow {
    @apply px-4 py-2 text-sm text-white font-bold rounded-2xl me-4 my-2 hover:opacity-70 transition ease-in-out duration-200;
}
</style>
<template>
    <div class="stories-wrap w-full flex justify-center py-0 sm:py-12">
        <div
            class="story-content min-h-full px-4 py-5 flex flex-col justify-between rounded-none md:rounded-2xl relative overflow-hidden">
            <div class="story-bar px-4 text-sm justify-between">
                <div class="flex items-center">
                    <div class="ml-6 sm:ml-0 bg-black size-10 rounded-xl flex justify-center items-center me-2">
                        <img class="size-7 rounded-full object-cover loading"
                            src="https://images.unsplash.com/photo-1519699047748-de8e457a634e?q=80&w=2960&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                            alt="">
                    </div>

                    <router-link to="Empty">@Nazariy</router-link>
                </div>

                <button class="rouded-full btn size-10 flex justify-center items-center text-sm">
                    <i class="fa-solid fa-volume-xmark"></i>
                </button>
            </div>

            <div class="story-bar justify-center">
                <button class="story-bar-button bg-red-400">
                    <i class="fa-solid fa-download"></i>
                </button>
                <button class="story-bar-button bg-purple-500">
                    <i class="fa-regular fa-heart"></i>
                </button>
                <button class="story-bar-button btn add-btn">
                    <i class="fa-solid fa-plus"></i>
                </button>
                <button class="story-bar-button bg-pink-500">
                    <i class="fa-solid fa-comment-dots"></i>
                </button>
                <button class="story-bar-button bg-blue-500">
                    <i class="fa-solid fa-circle-info"></i>
                </button>
            </div>

            <div class="absolute top-0 left-0 w-full h-full loading -z-10">
                <img class="w-full h-full object-cover"
                    src="https://images.unsplash.com/photo-1511860810434-a92f84c6f01e?q=80&w=2592&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                    alt="">
            </div>
        </div>
    </div>
</template>


<script>
export default {
    name: 'Story',
    setup() {

    }
}
</script>

<style>
.stories-wrap {
    min-height: 100vh;
}

.story-content {
    width: 400px;
}

.story-bar {
    @apply w-full h-14 bg-white rounded-2xl flex items-center;
}

.story-bar-button {
    @apply size-10 rounded-full mx-2 text-white flex justify-center items-center text-sm hover:opacity-85 hover:-translate-y-2 transition ease-linear duration-300;
}

.add-btn {
    @apply size-12 text-2xl;
}
</style>
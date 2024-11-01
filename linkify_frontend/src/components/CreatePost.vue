<template>
    <form @submit.prevent="createPost" class="mt-8 text-white font-medium space tracking-wider text-sm">
        <div class="flex flex-col justify-between items-center mb-4 sm:flex-row sm">
            <div class="min-w-40 min-h-40 max-w-40 max-h-40 rounded-full overflow-hidden loading 
            me-0 sm:me-4 mb-4 sm:mb-0 relative">
                <img class="absolute w-full h-full object-cover object-center"
                    src="https://images.unsplash.com/photo-1570158268183-d296b2892211?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8ZmFjZXxlbnwwfHwwfHx8MA%3D%3D"
                    alt="">
            </div>

            <div class="w-full min-h-40 flex flex-col justify-between">
                <input v-model="form.title"
                    class="w-full h-14 px-4 rounded-2xl bg-red-500 mb-4 sm:mb-0 placeholder-white" type="text"
                    placeholder="Title..">

                <div class="w-full grid grid-cols-2 gap-4 text-xl h-14">
                    <div class="w-full h-full">
                        <label for="img-input" class="w-full h-full">
                            <div class="w-full h-full rounded-2xl bg-emerald-500 flex justify-center items-center">
                                <i class="fa-solid fa-image"></i>
                            </div>
                        </label>
                        <input class="hidden" id="img-input" type="file" @change="handleImageInput" multiple>
                    </div>

                    <div class="w-full h-full">
                        <label for="video-input" class="w-full h-full">
                            <div class="w-full h-full rounded-2xl bg-purple-500 flex justify-center items-center">
                                <i class="fa-solid fa-video"></i>
                            </div>
                        </label>
                        <input class="hidden" id="video-input" type="file" @change="handleVideInput" multiple>
                    </div>
                </div>
            </div>
        </div>

        <div class="input-wrap w-full h-32">
            <textarea v-model="form.body"
                class="w-full h-full rounded-2xl p-4 bg-amber-500 resize-none placeholder-white"
                placeholder="Description.."></textarea>
        </div>

        <div class="w-full h-14 flex">
            <button type="submit" class="input-wrap btn h-full px-4 me-4">Create post</button>
            <button @click="resetForm" class="input-wrap btn h-full px-4">Reset</button>
        </div>
    </form>
</template>

<script>
    import { reactive } from 'vue'
    import axios from 'axios'

    export default {
        name: 'CreatePost',
        setup() {
            const form = reactive({
                'title': '',
                'body': '',
                'images': null,
                'videos': null,
            })


            function handleImageInput(event) {
                form.images = Array.from(event.target.files)
            }

            function handleVideoInput(event) {
                form.videos = Array.from(event.target.files)
            }

            function resetForm() {
                form.title = ''
                form.body = ''
                form.images = null
                form.videos = null
            }


            async function createPost() {
                const url = '/api/posts/create/'
                const user_access_token = localStorage.getItem('user.access')

                if (!user_access_token) return


                try {
                    const formData = new FormData()
                    formData.append('title', form.title)
                    formData.append('body', form.body)

                    if (form.images) {
                        form.images.forEach(image => {
                            formData.append('images', image)
                        })
                    }

                    if (form.videos) {
                        form.videos.forEach(video => {
                            formData.append('videos', video)
                        })
                    }
                    

                    const response = await axios.post(url, formData, {
                        headers: {
                            'Authorization': `Bearer ${user_access_token}`,
                            'Content-Type': 'multipart/form-data'
                        }
                    })

                    if (!response) return

                    console.log(response.data)

                    resetForm()
                } catch (error) {
                    console.log('Oops, Something went wrong :(', error)
                }
            }

            return { form, handleImageInput, handleVideoInput, resetForm, createPost }
        },
    }
</script>


<style>
    .input-wrap {
        @apply mb-8;
    }
</style>
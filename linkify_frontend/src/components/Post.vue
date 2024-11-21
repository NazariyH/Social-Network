<template>
    <div :class="['post-main-block', 'w-full', 'mb-8', 'rounded-3xl', 'p-8', 'text-white', 'font-bold', randomColor]"
        :data-postId="post.id">

        <div class="flex items-center justify-between w-ful mb-4">
            <router-link to="empty">
                <div class="flex items-center">
                    <div class="w-10 h-10 rounded-full overflow-hidden loading me-4">
                        <img class="w-full h-full object-cover"
                            src="https://images.unsplash.com/photo-1570158268183-d296b2892211?q=80&w=3087&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                            alt="Profile image">
                    </div>

                    <span v-if="post.author.name">{{ post.author.name }}</span>
                </div>
            </router-link>

            <div>
                <span v-if="post.created_at_formatted">{{ post.created_at_formatted }} ago</span>
            </div>
        </div>

        <div class="mb-4">
            <router-link :to="{ name: 'post-detail', params: { id: post.id } }">{{ post.title }}</router-link>
        </div>

        <div v-if="post.images.length !== 0 || post.videos.length !== 0"
            class="w-full rounded-3xl overflow-hidden mb-4">
            <div class="flex items-end w-full h-post-file relative">
                <div :data-postId="post.id"
                    class="slider-wrap w-full h-full loading absolute top-0 flex transition ease-linear duration-300">
                    <img v-for="image_obj in post.images" :src="image_obj.image" :key="image_obj.id" alt="image"
                        class="w-full h-full object-cover">
                </div>

                <div class="w-full h-20 relative slider-footer">
                    <div class="flex justify-center items-center w-full h-full absolute">
                        <span v-for="(image_obj, index) in post.images" :key="image_obj.id"
                            @click="toggleSlide($event, post.id)" :data-id="index"
                            :class="{ 'slider-dot': true, 'active': index === 0 }" :data-postId="post.id"></span>
                    </div>
                </div>
            </div>
        </div>

        <div v-if="post.body" class="mb-4">
            <p>{{ post.body }}</p>
        </div>

        <div class="flex justify-between w-full">
            <div class="flex">
                <div class="me-8">
                    <button class="like-btn">
                        <i v-if="!post.is_liked" class="fa-regular fa-heart"></i>
                        <i v-else class="fa-solid fa-heart"></i>

                        <span class="ml-4" v-if="post.likes_count">{{ post.likes_count }}</span>
                        <span class="ml-4" v-else>0</span>
                    </button>
                </div>

                <div>
                    <button>
                        <i class="fa-solid fa-comment-dots"></i>
                        <span v-if="post.comments_count" class="ml-4">{{ post.comments_count }}</span>
                        <span v-else class="ml-4">0</span>
                    </button>
                </div>
            </div>

            <div v-if="post.is_current_user" class="flex relative">
                <div 
                class="post-option-block hidden px-4 py-2 bg-gray-100 absolute 
                right-full bottom-0 text-black rounded-xl rounded-br-none text-sm" 
                :data-postId="post.id">
                    <ul>
                        <li class="post-option-menu-item">
                            <button><i class="fa-regular fa-bookmark"></i>Save</button>
                        </li>
                        <li class="post-option-menu-item">
                            <button><i class="fa-solid fa-pen-to-square"></i>Edit</button>
                        </li>
                        <li class="post-option-menu-item">
                            <button @:click="removePost(post.id)"><i class="fa-solid fa-trash"></i>Remove</button>
                        </li>
                    </ul>
                </div>

                <button @click="showPostOption($event)">
                    <i class="fa-solid fa-ellipsis rotate-90"></i>
                </button>
            </div>
        </div>
    </div>
</template>

<script>

import { onMounted, ref } from 'vue'
import { useColorsStore } from '@/store/colors'
import { useToastStore } from '@/store/toast.js'
import axios from 'axios'

export default {
    name: 'Post',
    props: ['post'],
    setup(props) {
        const sliderSwipeDistance = 100
        const colorsStore = useColorsStore()
        const toastStore = useToastStore()
        const randomColor = ref(colorsStore.getRandomColor())
        
        let postOptionBlock = null
        let touchStartX, touchEndX


        onMounted(() => {
            const sliderWrap = document.querySelector(`.post-main-block[data-postId="${props.post.id}"] .slider-wrap`)
            const sliderDots = document.querySelectorAll(`.post-main-block[data-postId="${props.post.id}"] .slider-dot`)
            postOptionBlock = document.querySelector(`.post-option-block[data-postId="${props.post.id}"]`)


            if (!sliderWrap && !sliderDots.length > 0) return

            sliderWrap.addEventListener('touchstart', event => {
                touchStartX = event.changedTouches[0].clientX
            })

            sliderWrap.addEventListener('touchend', event => {
                touchEndX = event.changedTouches[0].clientX
                handleTouch(sliderWrap, sliderDots)
            })
        })



        function handleTouch(sliderWrap, sliderDots) {
            let direction = null

            if (touchStartX - touchEndX > sliderSwipeDistance) direction = 'left'
            else if (touchEndX - touchStartX > sliderSwipeDistance) direction = 'right'

            if (direction) {
                const activeIndex = Array.from(sliderDots).findIndex(dot => dot.classList.contains('active'))
                let newIndex = activeIndex

                if (direction === 'left') {
                    newIndex = (activeIndex + 1) % sliderDots.length
                } else if (direction === 'right') {
                    newIndex = (activeIndex - 1 + sliderDots.length) % sliderDots.length
                }

                updateSlide(sliderWrap, sliderDots, newIndex)
            }

            touchEndX = 0
            touchStartX = 0
        }


        function updateSlide(sliderWrap, sliderDots, newIndex) {
            sliderDots.forEach(dot => dot.classList.remove('active'))
            sliderDots[newIndex].classList.add('active')

            sliderWrap.style.transform = `translateX(-${newIndex * 100}%)`
        }


        function toggleSlide(event, postId) {
            const sliderWrap = document.querySelector(`.post-main-block[data-postId="${postId}"] .slider-wrap`)
            const sliderDots = document.querySelectorAll(`.post-main-block[data-postId="${postId}"] .slider-dot`)
            const slideId = parseInt(event.target.getAttribute('data-id'))

            updateSlide(sliderWrap, sliderDots, slideId)
        }


        function showPostOption(event) {
            postOptionBlock.classList.toggle('hidden')
        }


        async function removePost(id) {
            const url = `/api/posts/${id}/delete/`

            try {
                const user_access_token = localStorage.getItem('user.access')
                const response = await axios.delete(url, {
                    headers: {
                        'Authorization': `Bearer ${user_access_token}`
                    }
                })


                const post = document.querySelector(`.post-main-block[data-postId="${id}"]`)
                post.remove()
                
                toastStore.showToast(5000, 'Your post has been succcessfully deleted', 'bg-emerald-600')
            } catch (error) {
                toastStore.showToast(5000, 'Something went wrong', 'bg-red-600')
            }
        }

        return { toggleSlide, randomColor, showPostOption, removePost }
    }
}


</script>


<style>
.slider-footer {
    background: linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1));
}

.slider-dot {
    @apply w-3 h-3 rounded-full bg-gray-300 mx-2 block cursor-pointer hover:bg-gray-400 transition ease-linear duration-200;
}

.slider-dot.active {
    @apply w-4 h-4 bg-gray-700 hover:bg-gray-600
}


.like-btn.liked {
    animation: bounce 0.6s;
}

@keyframes bounce {

    0%,
    20%,
    50%,
    80%,
    100% {
        transform: translateY(0);
    }

    40% {
        transform: translateY(-10px);
    }

    60% {
        transform: translateY(-5px);
    }
}

.slider-wrap img {
    min-width: 100%;
    max-width: 100%;
}

.post-option-menu-item {
    @apply m-2;
}

.post-option-menu-item button {
    @apply flex items-center hover:text-gray-500 transition ease-linear duration-200;
}

.post-option-menu-item button i {
    @apply me-4;
}
</style>
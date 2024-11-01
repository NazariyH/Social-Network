<template>
    <div :class="['w-full', 'mb-8', 'rounded-3xl', 'p-8', 'text-white', 'font-bold', randomColor]">
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
                <span v-if="post.created_at_formated">{{ post.created_at_formated }}</span>
            </div>
        </div>

        <div class="mb-4">
            <h1 v-if="post.title">{{ post.title }}</h1>
        </div>

        <div class="w-full rounded-3xl overflow-hidden mb-4">
            <div class="flex items-end w-full h-post-file relative">
                <div id="slider-wrap"
                    class="w-full h-full loading absolute top-0 flex transition ease-linear duration-300">
                    <img class="min-w-full h-full object-cover"
                        src="https://images.unsplash.com/photo-1498429089284-41f8cf3ffd39?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                        alt="File">
                    <img class="min-w-full h-full object-cover"
                        src="https://images.unsplash.com/photo-1500964757637-c85e8a162699?q=80&w=3303&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                        alt="File">
                    <img class="min-w-full h-full object-cover"
                        src="https://images.unsplash.com/photo-1451337516015-6b6e9a44a8a3?q=80&w=3174&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                        alt="File">
                    <img class="min-w-full h-full object-cover"
                        src="https://images.unsplash.com/photo-1494500764479-0c8f2919a3d8?q=80&w=3270&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                        alt="File">
                    <img class="min-w-full h-full object-cover"
                        src="https://images.unsplash.com/photo-1426604966848-d7adac402bff?q=80&w=3270&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                        alt="File">
                </div>

                <div id="slider-footer" class="w-full h-20 relative">
                    <div class="flex justify-center items-center w-full h-full absolute">
                        <span @click="toggleSlide($event)" data-id="1" class="slider-dot active"></span>
                        <span @click="toggleSlide($event)" data-id="2" class="slider-dot"></span>
                        <span @click="toggleSlide($event)" data-id="3" class="slider-dot"></span>
                        <span @click="toggleSlide($event)" data-id="4" class="slider-dot"></span>
                        <span @click="toggleSlide($event)" data-id="5" class="slider-dot"></span>
                    </div>
                </div>
            </div>
        </div>

        <div v-if="post.body" class="mb-4">
            <p>{{ post.body }}</p>
        </div>

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
    </div>
</template>

<script>
    import { onMounted } from 'vue'
    import { useColorsStore } from '@/store/colors'
    import { ref } from 'vue'

    export default {
        name: 'Post',
        props: ['post'],
        setup() {
            const colorsStore = useColorsStore()
            const randomColor = ref(colorsStore.getRandomColor())

            let currentSliderDot, sliderWrap, touchStartX, touchEndX, dots
            let currentSliderId = 0


            onMounted(() => {
                sliderWrap = document.getElementById('slider-wrap')
                dots = document.querySelectorAll('.slider-dot')

                sliderWrap.addEventListener('touchstart', event => {
                    touchStartX = event.changedTouches[0].clientX
                })

                sliderWrap.addEventListener('touchend', event => {
                    touchEndX = event.changedTouches[0].clientX
                    handleTouch()
                })
            })



            function handleTouch() {
                if (touchEndX - touchStartX > 100) {
                    currentSliderId--

                    if (currentSliderId - 1 < -1)
                        currentSliderId = dots.length - 1


                    toggleSlide(dots[currentSliderId])
                }

                if (touchEndX - touchStartX < -100) {
                    currentSliderId++

                    if (currentSliderId + 1 > dots.length)
                        currentSliderId = 0

                    toggleSlide(dots[currentSliderId])
                }
            }

            function toggleSlide(event) {
                let slideId

                currentSliderDot = document.querySelector('.slider-dot.active')
                currentSliderDot.classList.remove('active')

                if (event.currentTarget) {
                    event.currentTarget.classList.add('active')
                    slideId = event.currentTarget.getAttribute('data-id') - 1
                    currentSliderId = slideId

                } else {
                    event.classList.add('active')
                    slideId = event.getAttribute('data-id') - 1
                }

                sliderWrap.style.transform = `translateX(-${slideId}00%)`
            }


            return { toggleSlide, randomColor }

        }
    }
</script>


<style>
    #slider-footer {
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
    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-10px); }
    60% { transform: translateY(-5px); }
}
</style>
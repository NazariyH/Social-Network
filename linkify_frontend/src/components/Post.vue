<template>
    <div class="w-full mb-8 rounded-3xl bg-purple-500 p-8 text-white font-bold">
        <div class="flex items-center justify-between w-ful mb-4">
            <router-link to="empty">
                <div class="flex items-center">
                    <div class="w-10 h-10 rounded-full overflow-hidden loading me-4">
                        <img class="w-full h-full object-cover"
                            src="https://images.unsplash.com/photo-1570158268183-d296b2892211?q=80&w=3087&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                            alt="Profile image">
                    </div>

                    <span>Nazariy</span>
                </div>
            </router-link>

            <div>
                <span>20.10.2007</span>
            </div>
        </div>

        <div class="mb-4">
            <h1>Exploring the World: Hidden Gems in Popular Destinations</h1>
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

        <div class="mb-4">
            <p>Discover the lesser-known treasures nestled within popular travel destinations. This post takes you off
                the beaten path to unveil stunning landscapes, charming local spots, and unique cultural experiences
                that often go unnoticed. From secret beaches to quaint cafes, explore how these hidden gems can
                transform your travels and offer a deeper connection to the places you visit. Join us on this journey to
                uncover the world’s best-kept secrets!</p>
        </div>

        <div class="flex">
            <div class="me-8">
                <button class="like-btn">
                    <i class="fa-regular fa-heart"></i>
                    <span class="ml-4">732</span>
                </button>
            </div>

            <div>
                <button>
                    <i class="fa-solid fa-comment-dots"></i>
                    <span class="ml-4">24</span>
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    import { onMounted } from 'vue'
    export default {
        name: 'Post',
        props: ['post'],
        setup() {
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
                    console.log(event.currentTarget)
                    event.currentTarget.classList.add('active')
                    slideId = event.currentTarget.getAttribute('data-id') - 1
                    currentSliderId = slideId

                } else {
                    console.log(event)
                    event.classList.add('active')
                    slideId = event.getAttribute('data-id') - 1
                }

                sliderWrap.style.transform = `translateX(-${slideId}00%)`
            }


            return { toggleSlide }

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
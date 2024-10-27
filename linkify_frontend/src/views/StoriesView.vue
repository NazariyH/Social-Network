<template>
    <div class="w-full overflow-hidden">
        <div id="story-screen" class="w-full flex flex-col transition ease-linear duration-300">
            <Story />
            <Story />
            <Story />
            <Story />
            <Story />
            <Story />
        </div>
    </div>
</template>


<script>
import Story from '@/components/Story.vue'

import { onMounted } from 'vue'

export default {
    name: 'StoriesView',
    components: {
        Story
    },
    setup() {
        let storiesWrap, storyScreen, touchScreenStart, touchScreenEnd
        let storyPosition = 0, swipeRange = 100


        onMounted(() => {
            storiesWrap = document.querySelectorAll('.stories-wrap')
            storyScreen = document.getElementById('story-screen')


            document.addEventListener('keydown', event => {
                if (event.code === 'ArrowDown')
                    moveStories('down')
                else if (event.code === 'ArrowUp')
                    moveStories('up')
            })

            document.addEventListener('touchstart', event => {
                touchScreenStart = event.changedTouches[0].clientY
            })

            document.addEventListener('touchend', event => {
                touchScreenEnd = event.changedTouches[0].clientY
                handleStorySwipe()
            })
        })


        function moveStories(direction) {
            if (direction === 'down') {
                storyPosition += 1

                storyScreen.style.transform = `translateY(-${storyPosition}00%)`
            } else if (direction === 'up') {
                if (storyPosition !== 0)
                    storyPosition -= 1

                storyScreen.style.transform = `translateY(-${storyPosition}00%)`
            }
        }

        function handleStorySwipe() {
            if(touchScreenEnd - touchScreenStart > swipeRange)
                moveStories('up')

            if(touchScreenEnd - touchScreenStart < -swipeRange)
                moveStories('down')
        }
    }
}
</script>

<style>
#story-screen {
    max-height: 100vh;
}
</style>
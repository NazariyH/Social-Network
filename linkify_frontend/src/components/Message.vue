<template>
    <div class="w-full flex receiver text-white mb-16">
        <div class="max-w-64 min-w-16 h-auto py-2 px-4 relative rounded-2xl">
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta distinctio reprehenderit mollitia nisi
                quae nemo?</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Message',
        setup() {

        }
    }
</script>

<style>
    .sender {
        @apply justify-end;
    }

    .sender>div {
        @apply bg-blue-600 rounded-br-none after:absolute after:-bottom-8 after:right-0 after:w-0 after:h-0 after:border-t-[0px] after:border-b-[40px] after:border-r-[75px] after:border-transparent after:border-r-blue-600;
    }


    .receiver {
        @apply justify-start;
    }

    .receiver>div {
        @apply bg-pink-600 rounded-bl-none after:absolute after:-bottom-8 after:left-0 after:w-0 after:h-0 after:border-t-[0px] after:border-b-[40px] after:border-l-[75px] after:border-transparent after:border-l-pink-600;
    }
</style>
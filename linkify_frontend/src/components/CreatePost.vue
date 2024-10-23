<template>
    <form class="mt-8 text-white font-medium space tracking-wider">
        <div class="flex flex-col justify-between items-center mb-4 sm:flex-row sm">
            <div class="min-w-40 min-h-40 max-w-40 max-h-40 rounded-full overflow-hidden loading 
            me-0 sm:me-4 mb-4 sm:mb-0 relative">
                <img class="absolute w-full h-full object-cover object-center"
                    src="https://images.unsplash.com/photo-1570158268183-d296b2892211?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8ZmFjZXxlbnwwfHwwfHx8MA%3D%3D"
                    alt="">
            </div>            

            <div class="w-full min-h-40 flex flex-col justify-between">
                <input class="w-full h-16 px-4 rounded-2xl bg-red-500 mb-4 sm:mb-0 placeholder-white" type="text" placeholder="Title..">

                <div class="w-full grid grid-cols-2 gap-4 text-2xl h-16">
                    <div class="w-full h-full">
                        <label for="img-input" class="w-full h-full">
                            <div class="w-full h-full rounded-2xl bg-emerald-500 flex justify-center items-center">
                                <i class="fa-solid fa-image"></i>
                            </div>
                        </label>
                        <input class="hidden" id="img-input" type="file" multiple>
                    </div>

                    <div class="w-full h-full">
                        <label for="video-input" class="w-full h-full">
                            <div class="w-full h-full rounded-2xl bg-purple-500 flex justify-center items-center">
                                <i class="fa-solid fa-video"></i>
                            </div>
                        </label>
                        <input class="hidden" id="video-input" type="file" multiple>
                    </div>
                </div>
            </div>
        </div>

        <div class="input-wrap w-full h-32">
            <textarea class="w-full h-full rounded-2xl p-4 bg-amber-500 resize-none placeholder-white" placeholder="Description.."></textarea>
        </div>
    </form>
</template>

<script>
    export default {
        name: 'CreatePost',
        setup() {

        }
    }
</script>


<style>
    .input-wrap {
        @apply mb-8;
    }
</style>
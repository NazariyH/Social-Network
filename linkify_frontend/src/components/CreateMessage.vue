<template>
    <div>
        <form class="flex text-white pt-4">
            <button type="submit" class="btn mr-2">Send</button>

            <input class="create-message-block bg-red-400 w-full px-4 placeholder-white" placeholder="Your message.." type="text">

            <div class="mx-2">
                <label class="create-message-block bg-purple-400" for="img">
                    <i class="fa-solid fa-image"></i>
                </label>
                <input id="img" class="hidden" type="file" multiple>
            </div>

            <div>
                <label class="create-message-block bg-amber-400" for="video">
                    <i class="fa-solid fa-video"></i>
                </label>
                <input id="video" class="hidden" type="file">
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: 'CreateMessage',
    setup() {

    }
}
</script>


<style>
.create-message-block {
    @apply h-14 rounded-2xl py-2 py-4 flex justify-center items-center;
}

label.create-message-block,
form button {
    @apply min-w-14 ;
}
</style>
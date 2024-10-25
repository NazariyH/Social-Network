<template>
    <div id="friendbar-wrap">
        <div @click="toggleMenu($event)" id="friendbar-toggle-btn" class="bar-block">
            <div class="w-full h-full relative">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>

        <div id="friendbar" class="w-auto rounded-3xl h-full bg-purple-500 flex-col 
        px-2 py-4 ml-4 hidden md:flex justify-center">
            <div class="flex h-12">
                <div class="bar-block min-w-40 me-20 btn toggle-item hidden-item">
                    <i class="fa-solid fa-plus"></i>
                </div>
            </div>

            <div class="overflow-y-auto h-full mt">



                <div class="h-full flex flex-col justify-center">
                    <div class="friend-block">
                        <div class="bar-block loading">
                            <span class="online-status"></span>
                            <img class="w-full h-full object-cover"
                                src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZmFjZXxlbnwwfHwwfHx8MA%3D%3D">
                        </div>
                        <h4 class="friend-name toggle-item hidden-item">Hermana</h4>
                    </div>
                    <div class="friend-block">
                        <div class="bar-block loading">
                            <span class="online-status active"></span>
                            <img class="w-full h-full object-cover"
                                src="https://images.unsplash.com/photo-1468218457742-ee484fe2fe4c?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fGZhY2V8ZW58MHx8MHx8fDA%3D">
                        </div>
                        <h4 class="friend-name toggle-item hidden-item">Padre</h4>
                    </div>
                    <div class="friend-block">
                        <div class="bar-block loading">
                            <span class="online-status active"></span>
                            <img class="w-full h-full object-cover"
                                src="https://images.unsplash.com/photo-1468218457742-ee484fe2fe4c?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fGZhY2V8ZW58MHx8MHx8fDA%3D">
                        </div>
                        <h4 class="friend-name toggle-item hidden-item">Padre</h4>
                    </div>
                    <div class="friend-block">
                        <div class="bar-block loading">
                            <span class="online-status"></span>
                            <img class="w-full h-full object-cover"
                                src="https://images.unsplash.com/photo-1599870418764-c38abcfb955a?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OTV8fGZhY2V8ZW58MHx8MHx8fDA%3D">
                        </div>
                        <h4 class="friend-name toggle-item hidden-item">Hermano</h4>
                    </div>
                    <div class="friend-block">
                        <div class="bar-block loading">
                            <span class="online-status active"></span>
                            <img class="w-full h-full object-cover"
                                src="https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mzl8fGZhY2V8ZW58MHx8MHx8fDA%3D">
                        </div>
                        <h4 class="friend-name toggle-item hidden-item">Madre</h4>
                    </div>
                    <div class="friend-block">
                        <div class="bar-block loading">
                            <span class="online-status"></span>
                            <img class="w-full h-full object-cover"
                                src="https://images.unsplash.com/photo-1493106819501-66d381c466f1?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGZhY2V8ZW58MHx8MHx8fDA%3D">
                        </div>
                        <h4 class="friend-name toggle-item hidden-item">Abuelo</h4>
                    </div>
                    <div class="friend-block">
                        <div class="bar-block loading active">
                            <span class="online-status"></span>
                            <img class="w-full h-full object-cover"
                                src="https://images.unsplash.com/photo-1519699047748-de8e457a634e?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NzB8fGZhY2V8ZW58MHx8MHx8fDA%3D">
                        </div>
                        <h4 class="friend-name toggle-item hidden-item">Nazariy</h4>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { onMounted } from 'vue'

export default {
    name: 'FriendBar',
    setup() {
        let toggleItems, friendbar

        onMounted(() => {
            toggleItems = document.querySelectorAll('.toggle-item')
            friendbar = document.getElementById('friendbar')
        })

        function toggleMenu(event) {
            event.currentTarget.classList.toggle('active')
            toggleItems.forEach(item => item.classList.toggle('hidden-item'))
            friendbar.classList.toggle('hidden')
        }

        return { toggleMenu }
    }
}
</script>


<style>
#friendbar-toggle-btn {
    @apply w-16 bg-white py-4 px-4 absolute top-12 right-6 cursor-pointer;
}

#friendbar-toggle-btn span {
    @apply w-full h-0.5 bg-black transition ease-linear duration-300 absolute right-0;
}

#friendbar-toggle-btn span:nth-child(2) {
    @apply w-4 top-1/2 -translate-y-1/2;
}

#friendbar-toggle-btn span:nth-child(3) {
    @apply w-5 bottom-0;
}

#friendbar-toggle-btn.active span {
    @apply absolute top-1/2 -translate-y-1/2;
}

#friendbar-toggle-btn.active span {
    @apply w-full;
}

#friendbar-toggle-btn.active span:nth-child(1) {
    @apply rotate-45;
}

#friendbar-toggle-btn.active span:nth-child(2) {
    @apply hidden;
}

#friendbar-toggle-btn.active span:nth-child(3) {
    @apply -rotate-45;
}

.bar-block {
    @apply w-12 h-12 rounded-2xl flex justify-center items-center relative;
}

.bar-block img {
    @apply rounded-2xl;
}

.friend-block {
    @apply p-2 bg-white rounded-2xl my-2 flex items-center cursor-pointer;
}

.friend-name {
    @apply ml-4;
}

.online-status.active {
    @apply size-2 bg-green-400 absolute top-0 right-0 rounded-full;
}

.hidden-item {
    display: none !important;
}
</style>
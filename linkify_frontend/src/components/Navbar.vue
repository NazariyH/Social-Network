<template>
    <div id="navbar-wrap" class="side-block active sticky top-0">
        <div @click="toggleMenu($event)" id="navbar-toggle-btn">
            <span></span>
            <span></span>
            <span></span>
        </div>

        <nav class="w-full h-full p-8 flex flex-col justify-between items-center">
            <div id="navbar-profile-info" class="w-full hidden">
                <div class="relative flex justify-end">
                    <img src="../assets/Decorations/profile_doodles.png" class="w-36 absolute -z-10 left-0">
                    <div class="w-36 h-36 loading rounded-full overflow-hidden">
                        <img class="w-full h-full object-cover"
                            src="https://images.unsplash.com/photo-1650630729397-810915b32ac9?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                            alt="profile image">
                    </div>
                </div>

                <h1 class="text-center text-2xl mt-4 font-bold">Nazariy</h1>
            </div>



            <ul class="text-sm w-full">
                <li class="navbar-tab active">
                    <router-link :to="{ name: 'home' }" class="flex items-center"><i class="fa-solid fa-compass text-xl mr-6"></i><span
                            class="navbar-text-link hidden">News Feed</span></router-link>
                </li>
                <li class="navbar-tab">
                    <router-link class="flex items-center"><i class="fa-solid fa-message text-xl mr-6"></i><span
                            class="navbar-text-link hidden">Messages</span></router-link>
                    <div class="badge hidden">3</div>
                </li>
                <li class="navbar-tab">
                    <router-link class="flex items-center"><i class="fa-solid fa-comment-dots text-xl mr-6"></i><span
                            class="navbar-text-link hidden">Forums</span></router-link>
                </li>
                <li class="navbar-tab">
                    <router-link class="flex items-center"><i class="fa-solid fa-user-group text-xl mr-5"></i><span
                            class="navbar-text-link hidden">Friends</span></router-link>
                    <div class="badge hidden">7</div>
                </li>
                <li class="navbar-tab">
                    <router-link class="flex items-center"><i class="fa-regular fa-image text-xl mr-6"></i><span
                            class="navbar-text-link hidden">Media</span></router-link>
                </li>
                <li class="navbar-tab">
                    <router-link :to="{ name: 'authentication' }" class="flex items-center"><i
                            class="fa-solid fa-gear text-xl mr-6"></i><span class="navbar-text-link hidden">Settings &
                            Account</span></router-link>
                </li>
            </ul>

            <p class="text-sm copy-rigth hidden">© 2024 Linkify. All rights reserved.</p>
        </nav>
    </div>
</template>


<script>
    import { onMounted } from 'vue'
    export default {
        name: 'Navbar',
        setup() {
            let navbarTextLinks, navbarProfileInfo, copyRight, badges, navbarWrap

            onMounted(() => {
                navbarTextLinks = document.querySelectorAll('.navbar-text-link')
                navbarProfileInfo = document.getElementById('navbar-profile-info')
                copyRight = document.querySelector('.copy-rigth')
                badges = document.querySelectorAll('.badge')
                navbarWrap = document.getElementById('navbar-wrap')
            })


            const toggleMenu = (event) => {
                event.currentTarget.classList.toggle('active')

                navbarTextLinks.forEach(e => e.classList.toggle('hidden'))
                badges.forEach(e => e.classList.toggle('hidden'))
                navbarProfileInfo.classList.toggle('hidden')
                copyRight.classList.toggle('hidden')
                navbarWrap.classList.toggle('active')
                navbarWrap.classList.toggle('unactive')
            }

            return { toggleMenu }


        }
    }
</script>


<style>
    ul,
    li {
        margin: 0;
        padding: 0;
        list-style: none;
    }

    input {
        all: unset;
        box-sizing: border-box;
    }

    input:focus {
        border: none;
        box-sizing: border-box;
    }



    #navbar-toggle-btn {
        @apply absolute top-8 left-6 w-6 h-4 flex flex-col justify-between z-10;
    }

    #navbar-toggle-btn span {
        @apply w-full h-0.5 bg-black transition ease-in duration-200;
    }

    #navbar-toggle-btn.active span {
        @apply absolute top-1/2 -translate-y-1/2;
    }

    #navbar-toggle-btn.active span:nth-child(1) {
        @apply -rotate-45;
    }

    #navbar-toggle-btn.active span:nth-child(2) {
        @apply hidden;
    }

    #navbar-toggle-btn.active span:nth-child(3) {
        @apply rotate-45;
    }

    #navbar-wrap.active {
        @apply w-auto;
    }

    #navbar-wrap.unactive {
        @apply min-w-80;
    }

    #navbar-wrap.active nav {
        @apply justify-center px-2;
    }

    #navbar-wrap.active nav li {
        @apply justify-center;
    }

    #navbar-wrap.active nav a,
    #navbar-wrap.active nav i {
        @apply m-0 p-0;
    }

    .navbar-tab {
        @apply flex items-center justify-between font-medium my-6 w-full py-2 px-4 cursor-pointer;
    }


    .navbar-tab.active {
        @apply bg-black text-white rounded-2xl;
    }

    .badge {
        @apply flex justify-center items-center w-6 h-6 text-sm rounded-full bg-black text-white;
    }

    .navbar-tab.active .badge {
        @apply bg-white text-black;
    }

    nav .hidden {
        display: none;
    }
</style>
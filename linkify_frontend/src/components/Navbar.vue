<template>
    <div id="navbar-wrap" class="side-block active sticky top-0 z-10">
        <div @click="toggleMenu" id="navbar-toggle-btn">
            <span></span>
            <span></span>
            <span></span>
        </div>

        <nav class="w-full h-full p-8 flex flex-col justify-between items-center overflow-y-auto">
            <div id="navbar-profile-info" class="w-full hidden navbar-item">
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
                <li>
                    <router-link :to="{ name: 'home' }" class="navbar-tab flex items-center">
                        <div>
                            <i class="fa-solid fa-compass text-xl mr-6"></i>
                            <span class="navbar-item hidden">News Feed</span>
                        </div>
                    </router-link>
                </li>
                <li @click="openMenu" class="navbar-tab" id="search-field-tab">
                    <i class="fa-solid fa-magnifying-glass"></i>

                    <form>
                        <input type="text" class="navbar-item hidden" id="search-field-input">
                    </form>
                </li>
                <li>
                    <router-link :to="{ name: 'inbox' }" class="navbar-tab flex items-center">
                        <div>
                            <i class="fa-solid fa-message text-xl mr-6"></i>
                            <span class="navbar-item hidden">Messages</span>
                        </div>

                        <div class="navbar-item hidden">3</div>
                    </router-link>
                </li>
                <li>
                    <button id="notification-btn" @click="toggleNotification" class="navbar-tab flex items-center">
                        <div>
                            <i class="fa-solid fa-bell text-xl mr-6"></i>
                            <span class="navbar-item hidden">Notifications</span>
                        </div>

                        <div class="navbar-item hidden">7</div>
                    </button>

                    <div id="notification-bar" class="hidden">
                        <Notification />
                    </div>
                </li>
                <li>
                    <router-link to="empty" class="navbar-tab flex items-center">
                        <div>
                            <i class="fa-solid fa-user-group text-xl mr-5"></i>
                            <span class="navbar-item hidden">Friends</span>
                        </div>

                        <div class="navbar-item hidden">7</div>
                    </router-link>
                </li>
                <li>
                    <router-link to="empty" class="navbar-tab flex items-center">
                        <div>
                            <i class="fa-regular fa-image text-xl mr-6"></i>
                            <span class="navbar-item hidden">Gallery</span>
                        </div>
                    </router-link>
                </li>
                <li>
                    <router-link :to="{ name: 'authentication' }" class="navbar-tab flex items-center">
                        <div>
                            <i class="fa-solid fa-gear text-xl mr-6"></i>
                            <span class="navbar-item hidden">Settings & Account</span>
                        </div>
                    </router-link>
                </li>
            </ul>

            <p class="text-sm hidden navbar-item">© 2024 Linkify. All rights reserved.</p>
        </nav>
    </div>
</template>


<script>
import { onMounted } from 'vue'
import Notification from '@/components/Notification.vue'

export default {
    name: 'Navbar',
    components: {
        Notification
    },
    setup() {
        let navbarItem, navbarWrap, navbarBtn, notificationBar, notificationBtn, 
        searchFieldInput, searchFieldTab

        onMounted(() => {
            navbarItem = document.querySelectorAll('.navbar-item')
            navbarWrap = document.getElementById('navbar-wrap')
            navbarBtn = document.getElementById('navbar-toggle-btn')
            notificationBar = document.getElementById('notification-bar')
            notificationBtn = document.getElementById('notification-btn')

            searchFieldInput = document.getElementById('search-field-input')
            searchFieldTab = document.getElementById('search-field-tab')

            searchFieldInput.addEventListener('focus', () => searchFieldTab.classList.add('active'))
            searchFieldInput.addEventListener('blur', () => searchFieldTab.classList.remove('active'))
        })


        const toggleMenu = () => {
            navbarBtn.classList.toggle('active')

            navbarItem.forEach(e => e.classList.toggle('hidden'))
            navbarWrap.classList.toggle('active')
            navbarWrap.classList.toggle('unactive')

            if (!notificationBar.classList.contains('hidden')) {
                notificationBtn.classList.remove('active')
                notificationBar.classList.add('hidden')
            }
        }


        const openMenu = () => {
            navbarBtn.classList.add('active')

            navbarItem.forEach(e => e.classList.remove('hidden'))
            navbarWrap.classList.remove('active')
            navbarWrap.classList.add('unactive')
        }


        const toggleNotification = () => {
            notificationBtn.classList.toggle('active')
            notificationBar.classList.toggle('hidden')

            if (navbarWrap.classList.contains('active')) {
                openMenu()
            }
        }

        return { toggleMenu, openMenu, toggleNotification }
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

#navbar-toggle-btn {
    @apply absolute top-8 left-4 w-10 h-8 flex flex-col justify-between z-10 bg-white p-2 rounded-md;
}
#navbar-toggle-btn.active {
    @apply left-6 p-2;
}

#navbar-toggle-btn span {
    @apply w-6 h-0.5 bg-black transition ease-in duration-200;
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
    @apply hidden md:flex;
}

#navbar-wrap.active nav {
    @apply justify-center px-2;
}

#navbar-wrap.active nav .navbar-tab {
    @apply justify-center my-4;
}

#navbar-wrap.active nav i {
    @apply m-0 p-0;
}

.navbar-tab {
    @apply flex items-center justify-between font-medium my-6 w-full py-2 px-2 sm:px-4 cursor-pointer;
}

.navbar-tab i {
    @apply text-xl;
}

.navbar-tab input {
    @apply px-2 py-1 rounded-xl bg-gray-100 h-10;
}

.navbar-tab.router-link-active,
.navbar-tab.active {
    @apply bg-black text-white rounded-2xl py-2 px-2 sm:px-4;
}

.navbar-tab.active input {
    @apply bg-white text-black;
}

.badge {
    @apply flex justify-center items-center w-6 h-6 text-sm rounded-full bg-black text-white;
}

.navbar-tab.router-link-active .badge,
.navbar-tab.active .badge {
    @apply bg-white text-black;
}

nav .hidden {
    display: none;
}
</style>
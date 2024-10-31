<template>
    <div class="h-auto w-full md:w-profile-view text-black p-4 md:pl-0">
        <ProfileInfo :profile="profile" />

        <div class="mt-4">
            <Post />
            <Post />
            <Post />
            <Post />
            <Post />
            <Post />
            <Post />
            <Post />
            <Post />
        </div>
    </div>
</template>


<script>
import ProfileInfo from '@/components/ProfileInfo.vue'
import Post from '@/components/Post.vue'
import { ref } from 'vue'

export default {
    name: 'ProfileView',
    components: {
        ProfileInfo,
        Post,
    },
    setup() {
        const profile = ref({
            email: 'test1@gmail.com',
            name: 'Mis Hermano',
            age: 96,
            friendsCount: 324,
            origin: 'Spanish',
            bio: 'fkjasfdjklsajfksjdfklsajdfjdskfasdfjaskdlfjskdafkjasfdjklsajfksjdfklsajdfjdskfasdfjaskdlfjskdafkjasfdjklsajfksjdfklsajdfjdskfasdfjaskdlfjskdafkjasfdjklsajfksjdfklsajdfjdskfasdfjaskdlfjskdafkjasfdjklsajfksjdfklsajdfjdskfasdfjaskdlfjskdafkjasfdjklsajfksjdfklsajdfjdskfasdfjaskdlfjskdafkjasfdjklsajfksjdfklsajdfjdskfasdfjaskdlfjskda',
            profileImage: 'https://images.unsplash.com/photo-1570158268183-d296b2892211?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8ZmFjZXxlbnwwfHwwfHx8MA%3D%3D',
            goals: ['Love', 'Life','Love', 'Life', 'Love', 'Life','Love', 'Life', 'Love', 'Life','Love', 'Life', 'Love', 'Life','Love', 'Life', 'Love', 'Life','Love', 'Life', 'Love', 'Life','Love', 'Life', 'Love', 'Life','Love', 'Life'],
            socialMedias: [['x', '#'], ['reddit', '#'], ['telegram', '#'], ['instagram', '#']],
            isCurrentUser: true,
        })


        return { profile }
    }
}
</script>

<template>
    <div>Hello Worl</div>
</template>


<script>
import { useRoute } from 'vue-router'
export default {
    name: 'PostDetailView',
    setup() {
        const route = useRoute()
        const postId = route.params.id
        console.log(postId)

        return {}
    }
}
</script>
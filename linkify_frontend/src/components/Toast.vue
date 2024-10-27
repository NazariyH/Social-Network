<template>
    <div v-if="store.isVisible" 
    class="transition ease-in-out delay-500 duration-300 p-6" 
    :class="store.classes">{{ store.message }}</div>
</template>

<script>
export default {
    name: 'Toast',
    setup() {

    }
}
</script>
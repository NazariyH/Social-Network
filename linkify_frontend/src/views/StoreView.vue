<template>
    <div class="w-full p-2">
        <div class="pl-16 md:pl-4 w-full rounded-2xl bg-black py-4 px-4 text-white mb-4">
            <div class="flex justify-between items-center w-full">
                <div class="flex items-center">
                    <div class="min-w-12 h-12 me-4 p-2 relative rounded-2xl bg-white  cursor-pointer">
                        <div class="w-full h-full rounded-full loading relative overflow-hidden">
                            <img class="absolute w-full h-full object-cover"
                                src="https://images.unsplash.com/photo-1542513217-0b0eedf7005d?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTA2fHxmYWNlfGVufDB8fDB8fHww"
                                alt="">
                        </div>
                    </div>
                    <span>@Nazariy</span>
                </div>

                <div class="flex items-center">
                    <span class="me-4">0</span>
                    <i class="fa-brands fa-bitcoin text-2xl"></i>
                </div>
            </div>
        </div>

        <div class="px-4 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-5 gap-8">
            <EmojiCard />
            <EmojiCard />
            <EmojiCard />
            <EmojiCard />
            <EmojiCard />
            <EmojiCard />
            <EmojiCard />
            <EmojiCard />
            <EmojiCard />
            <EmojiCard />
        </div>
    </div>

</template>


<script>
import EmojiCard from '@/components/EmojiCard.vue'

export default {
    name: 'StoreView',
    components: {
        EmojiCard
    },
    setup() {

    }
}
</script>
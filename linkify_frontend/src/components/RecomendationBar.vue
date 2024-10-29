<template>
    <div class="hidden side-block min-w-80 sticky top-0 max-w-0 lg:block">
        <div class="w-full h-full px-4 flex flex-col justify-between items-center top-0 right-0">
            <div>
                <div>
                    <h1 class="text-2xl font-bold mb-4">Stories</h1>

                    <div class="flex">
                        <div class="rounded-2xl h-40 w-32 loading mr-2 overflow-hidden relative">
                            <img class="w-full h-full object-cover"
                                src="https://images.unsplash.com/photo-1511860810434-a92f84c6f01e?q=80&w=2592&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                                alt="Story">
                            <div class="w-full px-2 absolute bottom-2 ">
                                <div class="w-full bg-white text-center text-sm font-bold rounded-2xl">Nazariy</div>
                            </div>
                        </div>
                        <div class="rounded-2xl h-40 w-32 loading overflow-hidden relative">
                            <img class="w-full h-full object-cover"
                                src="https://images.unsplash.com/photo-1541336032412-2048a678540d?q=80&w=3174&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                                alt="Story">
                            <div class="w-full px-2 absolute bottom-2 ">
                                <div class="w-full bg-white text-center text-sm font-bold rounded-2xl">Holovach</div>
                            </div>
                        </div>
                    </div>

                    <button class="btn w-full h-10 mt-4">New</button>
                </div>



                <div class="mt-8 w-full">
                    <h1 class="text-2xl font-bold mb-4">Suggestions</h1>

                    <div class="w-full">
                        <div class="flex justify-between items-center mt-2">
                            <div class="flex items-center">
                                <div class="w-10 h-10 loading rounded-full mr-2 overflow-hidden">
                                    <img src="https://plus.unsplash.com/premium_photo-1689977807477-a579eda91fa2?q=80&w=3270&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                                        class="w-full h-full object-cover">
                                </div>

                                <h1>Nazariy</h1>
                            </div>

                            <button class="py-1 px-4 btn text-sm">follow</button>
                        </div>

                        <div class="flex justify-between items-center mt-2">
                            <div class="flex items-center">
                                <div class="w-10 h-10 loading rounded-full mr-2 overflow-hidden">
                                    <img src="https://images.unsplash.com/photo-1531314888229-c4b4682c3118?q=80&w=3327&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                                        class="w-full h-full object-cover">
                                </div>

                                <h1>Holovach</h1>
                            </div>

                            <button class="py-1 px-4 btn text-sm">follow</button>
                        </div>

                        <div class="flex justify-between items-center mt-2">
                            <div class="flex items-center">
                                <div class="w-10 h-10 loading rounded-full mr-2 overflow-hidden">
                                    <img src="https://images.unsplash.com/photo-1531265180709-e9b5fb594ca6?q=80&w=3327&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                                        class="w-full h-full object-cover">
                                </div>

                                <h1>Romanovich</h1>
                            </div>

                            <button class="py-1 px-4 btn text-sm">follow</button>
                        </div>

                        <div class="flex justify-between items-center mt-2">
                            <div class="flex items-center">
                                <div class="w-10 h-10 loading rounded-full mr-2 overflow-hidden">
                                    <img src="https://plus.unsplash.com/premium_photo-1674777843203-da3ebb9fbca0?q=80&w=2473&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                                        class="w-full h-full object-cover">
                                </div>

                                <h1>Ura</h1>
                            </div>

                            <button class="py-1 px-4 btn text-sm">follow</button>
                        </div>

                    </div>
                </div>
            </div>

            <div>

            </div>
        </div>
    </div>
</template>


<script>
    export default {
        name: 'RecomendationBar',
        setup() {

        }
    }
</script>
<script setup lang="ts">
import { ref} from 'vue'
import toLearnItem from '~/components/Subject.vue'

    const topic = ref<string>("")
</script>

<template>
  <div  class="flex flex-col h-screen w-screen justify-center items-center gap-10 bg-black">
        <h1 class="text-lg text-gradienttext-3xl sm:text-4xl md:text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-red-400 to-blue-600 drop-shadow-lg">TO LEARN LIST</h1>
        <input v-model="topic" placeholder="What do you want to learn about" class="text-white h-10 w-1/2 bg-transparent border rounded-lg p-2"/>
  </div>
</template>

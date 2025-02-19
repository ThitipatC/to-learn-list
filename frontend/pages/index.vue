<script setup lang="ts">
import {ref, onMounted} from 'vue'
import { useRouter, useRuntimeConfig } from 'nuxt/app'
const topic = ref<string>("")
const config = useRuntimeConfig()
const router = useRouter()
const isFetching = ref<boolean>(false)
onMounted(() => console.log(`${config.public.BACKEND_URL}/tasks/generate-topics`))
const generateList = () => {
    isFetching.value = true;
    fetch(`${config.public.BACKEND_URL}/tasks/generate-topics`, {
      method : "POST",
      headers : {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ "topic": topic.value })
    }).then(res => res.json()).then(json_dict => JSON.stringify(json_dict.data)).then((info) => localStorage.setItem("topic", info)).then(() => router.push(`/subjects/${JSON.parse(localStorage.getItem("topic")).subject_name}`))
};
</script>

<template>
  <div class="flex flex-col h-screen w-screen justify-center items-center gap-10 bg-black">
    
    <!-- Spinner loader -->
    <div class="flex flex-col justify-center items-center gap-5" v-if="isFetching">
      <div class="h-10 w-10 rounded-full border-4 border-white border-t-transparent animate-spin"></div>
      <label class="text-white">generating your customized learning list </label>
    </div>
    
    <!-- Input and Button (conditionally rendered) -->
    <div v-else class="flex flex-col justify-center h-full w-full items-center gap-5">
      <h1 class="text-lg text-gradienttext-3xl sm:text-4xl md:text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-red-400 to-blue-600 drop-shadow-lg">
        TO LEARN LIST
      </h1>
      <input v-model="topic" placeholder="What do you want to learn about" class="text-white h-10 w-1/2 bg-transparent border rounded-lg p-2"/>
      <button class="border rounded-full p-2 bg-blue-500 text-white drop-shadow-l text-sm" @click="generateList()">START MY LEARNING JOURNEY!</button>
    </div>
  </div>
</template>


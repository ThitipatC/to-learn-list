<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute();
console.log(`route params are ${route.params}`)
const subject = route.params.subject
// fetch for corresponding topics and subtopics
const topics = ref([])
onMounted(() => {
   if (typeof window !== "undefined") {
      console.log(JSON.parse(localStorage.getItem("topic")).topics);
      topics.value = JSON.parse(localStorage.getItem("topic")).topics
   }
});
</script>

<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-100">
    <div class="w-3/4 max-w-4xl bg-white shadow-xl rounded-xl p-6">
    <h1 class="py-5"> My {{subject}} Learning Journey</h1>
      <div class="h-10 w-10 rounded-full animate-spin" v-if="topics.length === 0"/>
      <div v-else>
        <TopicLists v-for="(topic, index) in topics" :key = "index" :topic_name= "topic.topic_name" :subtopics ="topic.subtopics"/>
      </div>
    </div>
  </div>
</template>

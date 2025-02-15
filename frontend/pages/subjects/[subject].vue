<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute();
console.log(`route params are ${route.params}`)
const subject = route.params.subject
// fetch for corresponding topics and subtopics
const topics = ref([{topic_name : "react1", subtopics : [{subtopic_name: "s1", refs : ["s1-1.com", "s1-2.com"]}]},{topic_name : "react2", subtopics : [{subtopic_name: "s2", refs : ["s2-1.com", "s2-2.com"]}]}])

// onMounted(() => {
//   if (!localStorage.getItem("authToken")) {
//     router.push('/');
//   }
//   fetch('/your-api-endpoint') // Replace with your actual API endpoint
//     .then(res => res.json())
//     .then(data => {
//       subjects.value = data.data; // Adjust based on your API response structure
//     })
// });
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

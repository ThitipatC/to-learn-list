<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const subject = ref()

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
    <h1> My {{subject}} Learning Journey</h1>
      <div class="h-10 w-10 rounded-full animate-spin" v-if="subjects.length === 0"/>
      <div v-else>
        <p v-for="(subject, index) in subjects" :key="index">{{ subject }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { Status, SubjectProp } from '~/types'; // Import from the new types file
const items = ref<SubjectProp>([
  {status: "in progress", subject: "react", iconName: "logos:react"},
  {status: "in progress", subject: "Nuxt", iconName: "logos:nuxt-icon"}
    ])
</script>


<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-100">
    <div class="w-3/4 max-w-4xl bg-white shadow-xl rounded-xl p-6">
      <div class="flex items-center justify-between border-b pb-3">
        <h1 class="text-2xl font-semibold text-gray-700">📚 To Learn List</h1>
        <button class="px-3 py-1 bg-blue-500 text-white text-sm rounded-md hover:bg-blue-600 transition">
          + Add Topic
        </button>
      </div>
      <div class="mt-4 grid gap-3">
        <Subject  v-for="(item, index) in items" :subject="item.subject" :status="item.status" :iconName="item.iconName" :key="index"/>
      </div>
    </div>
  </div>
</template>


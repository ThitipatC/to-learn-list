<script setup lang="ts">
import { ref } from 'vue';
import { SubjectProp, Status } from '../components/Subject.vue';
const items = ref<SubjectProp[]>([
  {subject: "react", status: Status.InProgress,  iconName: "logos:react"},
  {subject: "nuxt", status: Status.InProgress, iconName: "logos:nuxt-icon"}
    ])
</script>


<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-100">
    <div class="w-3/4 max-w-4xl bg-white shadow-xl rounded-xl p-6">
      <div class="flex items-center justify-between border-b pb-3">
        <h1 class="text-2xl font-semibold text-gray-700">📚 To Learn List</h1>
        <button class="px-3 py-1 bg-blue-500 text-white text-sm rounded-md hover:bg-blue-600 transition" @click="$router.push('/')">
          + Add Topic
        </button>
      </div>
      <div class="mt-4 grid gap-3">
        <Subject  v-for="(item, index) in items" :subject="item.subject" :status="item.status" :iconName="item.iconName" :key="index"/>
      </div>
    </div>
  </div>
</template>


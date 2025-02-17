<script setup lang="ts">

export interface SubTopicProps {
  subtopic_name: string;
  refs: string[];  // Renamed from 'ref' to 'refs' to avoid conflicts
}

const props = defineProps<SubTopicProps>();
</script>

<template>
  <div class="flex flex-col">
    <h1 class="text-lg">{{ subtopic_name }}</h1>
    <ul>
      <li v-for="(item, index) in refs" :key="index">
        <a :href="item" target="_blank" class="text-blue-500 underline">{{ item }}</a>
      </li>
    </ul>
  </div>
</template>

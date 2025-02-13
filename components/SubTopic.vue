<script setup lang="ts">
import {Status} from "./Subject.vue"
export default interface subTopicProps {
  title: string
  concepts: string
  ref: string
  status: Status
}
const props = defineProps<toLearnprops>()
</script>

<template>
  <div class="flex">
    <h1 class="text-lg">{{title}}</h1>
    <li>{{concepts}}</li>
    <li><a :href="ref">ref</a></li>
  </div>
</template>
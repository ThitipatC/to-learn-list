<script setup lang="ts">
import SubTopicProps  from "./SubTopic.vue"
import {Status} from "./Subject.vue"
export default interface TopicListProps {
  topic: string
  status: Status
  subtopics: SubTopicProps[]
}
const props = defineProps<TopicListProps>()
</script>

<template>
  <div class="flex justify-between items-center p-3 border rounded-md bg-gray-50">
    <div class="flex items-center space-x-3">
      <div class="p-2 bg-blue-100 text-blue-600 rounded-full">
        <Icon :name="iconName" size="1.5em" />
      </div>
      <div>
        <p class="text-gray-800 font-medium">{{ subject }}</p>
      </div>
    </div>
    <span :class="status === Status.InProgress ? 'text-green-500' : 'text-red-500'">{{status}}</span>
  </div>
</template>
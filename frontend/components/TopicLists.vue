<script setup lang="ts">
  import {SubTopicProps} from "./SubTopic.vue"
  import { ref} from 'vue'
  interface TopicListProps {
  topic_name: string
  subtopics: SubTopicProps[]
}
const isClicked = ref<boolean>(false)
const props = defineProps<TopicListProps>()
</script>

<template>
<div>
<button class="flex w-full justify-between items-center p-3 border rounded-md bg-gray-50 border m-1" @click="isClicked = !isClicked"> 
                {{topic_name}} 
  </button>
  <div v-if="isClicked">
        <ul>
        <li class="mx-12 list-disc" v-for="(subtopic, index) in subtopics" :key="index">
            <SubTopic :subtopic_name="subtopic.subtopic_name" :refs = "subtopic.refs"/>
        </li>
        </ul>        
  </div>
</div>

</template>
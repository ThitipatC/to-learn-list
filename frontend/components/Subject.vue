
<script lang="ts">
export enum Status {
  InProgress = 'in progress',
  Completed = 'completed',
  Pending = 'pending'
}

export type SubjectProp = {
  subject: string;
  status: Status;
  iconName: string;
};

</script>
<script setup lang="ts">
const props = defineProps<SubjectProp>()
</script>


<template>
  <div class="flex justify-between items-center p-3 border rounded-md bg-gray-50">
    <div class="flex items-center space-x-3">
      <div class="p-2 bg-blue-100 text-blue-600 rounded-full">
        <Icon :name="iconName" size="1.5em" />
      </div>
      <div>
        <a href="" class="text-gray-800 font-medium">{{ subject }}</a>
      </div>
    </div>
    <span :class="status === Status.InProgress ? 'text-green-500' : 'text-red-500'">{{status}}</span>
  </div>
</template>
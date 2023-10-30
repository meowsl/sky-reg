<template>
  <div class="schedule-page">
    <p class="text-h4 font-weight-bold">Расписание</p>
    <div class="mt-6 d-flex justify-center align-center">
      <client-only>
        <VDatePicker
          :min-date="new Date()"
          trim-weeks
          class="vc"
          v-model="date"
          :attributes="attrs"
        />
      </client-only>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from '#imports'
const date = ref(new Date())

const attrs = ref([
  {
    key: 'today',
    highlight: {
      color: 'green',
      fillMode: 'solid'
    },
    dates: new Date(),


  }
])
</script>
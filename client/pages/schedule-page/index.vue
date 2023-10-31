<template>
  <div class="schedule-page">
    <p class="text-h4 font-weight-bold">Расписание</p>
    <div class="mt-6 d-flex justify-center align-center">
      <client-only>
        <VDatePicker
          :select-attribute="selectAttribute"
          :min-date="new Date()"
          trim-weeks
          class="vc"
          v-model="date"
          :attributes="attrs"
          :masks="{ title: 'MMM YYYY', weekdays: 'WW' }"
        />

      </client-only>

    </div>

  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const date = ref(new Date())
const selectAttribute = ref({
  highlight: {
    color: 'teal',
    fillMode: 'solid'

  }
})
const attrs = ref([
  {
    highlight: {
      color: 'green',
      fillMode: 'solid'
    },
    dates: new Date(),

  },
])
const popover = ref({
  visibility: 'hover',
  placement: 'right',
})
</script>
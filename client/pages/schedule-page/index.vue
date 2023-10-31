<template>
  <div class="schedule-page">
    <p class="text-h4 font-weight-bold">Расписание</p>
    <div class="mt-6 d-flex flex-column justify-center align-center">
      <client-only>
        <VDatePicker
          :select-attribute="selectAttribute"
          :attributes="attrs"
          :min-date="new Date()"
          trim-weeks
          class="vc"
          v-model="date"
          is-required
          :masks="masks"
        />
        <h1>{{ date }}</h1>
      </client-only>

      <VBtn variant="tonal"></VBtn>

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

const customer = reactive({
  name: 'Nathan Reyes',
  birthday: '1983-01-21',
})
const masks = ref({
  modelValue: 'YYYY-MM-DD',
  title: 'MMM YYYY',
  weekdays: 'WW'
})
</script>
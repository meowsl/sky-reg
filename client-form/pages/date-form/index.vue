<template>
  <VContainer
    class="form d-flex flex-column justify-space-between"
    style="border: 2px solid black !important; width: 75%; height: 80%;"
  >
    <div class="form__content-head px-16">
      <p
        class="form__title text-h5 font-weight-bold text-center py-6"
        style="color: #BB1F1B !important"
      >Записаться на прием</p>
      <VDivider />
    </div>
    <div class="form__content d-flex flex-column justify-start mt-16 h-75">
      <p class="text-h6 text-center text-black">Выберите дату и время</p>
      <VContainer class="w-75 mt-4">
        <div class="form__content__date-choise d-flex flex-column justify-center align-center">
          <p>Дата</p>
          <VDatePicker v-model="date">
            <template #default="{ inputValue, inputEvents }">
              <input
                :value="inputValue"
                v-on="inputEvents"
                class="px-2 py-1 bg-white d-flex justify-center"
                style="border: 1px solid black; height: 2.5rem;"
              />
            </template>
          </VDatePicker>
        </div>
      </VContainer>
    </div>
    <div class="form__content-foot d-flex flex-column justify-center px-16">
      <VDivider />
      <div class="d-flex flex-row justify-start align-center text-start">
        <NuxtLink
          to="/"
          class="d-flex flex-row align-center py-6"
        >
          <VImg
            :src="backArrow"
            width="40"
            height="40"
          />
          <p class="ms-4 text-h6">Назад</p>
        </NuxtLink>
      </div>
    </div>
  </VContainer>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import backArrow from 'images/backArrow.svg'

const menu = false
const date = ref(new Date())


const formattedDate = computed(() => {
  const day = date.value.getDate().toString().padStart(2, '0')
  const month = (date.value.getMonth() + 1).toString().padStart(2, '0')
  const year = date.value.getFullYear()
  return `${day}.${month}.${year}`
})
</script>
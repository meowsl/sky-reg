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
    <div class="form__content">
      <VContainer class="w-50">
        <p class="text-h6 text-center text-black">Выберите салон</p>
        <VSelect
          :items="items"
          v-model="model"
          density="compact"
          label="Адрес"
          class="mt-10"
          active="true"
          style="height: 5rem !important;"
        />
        <VBtn
          block="true"
          variant="flat"
          color="#BB1F1B"
          height="65"
          class="mt-16"
          @click="saveAddr()"
        >
          <p class="text-h5 text-white text-capitalize font-weight-bold">Продолжить</p>
        </VBtn>
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
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import backArrow from 'images/backArrow.svg'

const items = ['Ростов-на-Дону, ул. Обороны, 42Б', 'Краснодар, ул. Ставропольская, 127', 'Сочи, ул. Горького, 87']

const router = useRouter()
const savedType = ref()
const savedAddr = ref()

savedType.value = router.currentRoute.value.query.type
const model = ref()

function saveAddr() {
  savedAddr.value = model.value.split(',')[0].split('-')[0]
  router.push({
    path: '/date-form',
    query: {
      type: savedType.value,
      city: savedAddr.value,
    }
  })
}
</script>
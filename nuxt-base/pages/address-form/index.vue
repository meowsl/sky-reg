<template>
  <VContainer
    class="d-flex flex-column pb-16"
    style="border: 2px solid black !important; width: 75%; height: 80%;"
  >
    <p
      class="text-h5 font-weight-bold text-center mt-6"
      style="color: #BB1F1B !important"
    >Записаться на прием</p>
    <div class="mt-10">

      <VContainer class="w-50 mt-10">
        <p class="text-h6 text-center text-black">Выберите салон</p>
        <VSelect
          :items="items"
          density="compact"
          label="Адрес"
          class="mt-10"
          style="height: 5rem !important;"
        />
        <VBtn
          block="true"
          variant="flat"
          color="#BB1F1B"
          height="65"
          class="mt-16"
        >
          <p class="text-h5 text-white text-capitalize font-weight-bold">Продолжить</p>
        </VBtn>
      </VContainer>
    </div>
  </VContainer>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { ref } from 'vue'

const items = ['Ростов-на-Дону, ул. Обороны, 42Б', 'Краснодар, ул. Ставропольская, 127', 'Сочи, ул. Горького, 87']

const router = useRouter()
const savedType = ref()

savedType.value = router.currentRoute.value.query.typePriem
</script>
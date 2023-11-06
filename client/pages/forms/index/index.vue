<template>
  <VContainer
    class="px-16 d-flex flex-column w-auto justify-center"
    style="border:2px solid black !important; border-radius: 2% !important;"
  >
    <p
      class="form-title text-h5 text-center font-weight-bold"
      style="color:#BB1F1B !important "
    >Записаться на прием</p>
    <VRow class="mt-6">
      <VCol
        cols="4"
        class="d-flex flex-column align-center"
      >
        <p class="text-h6">Первичный прием</p>
        <VImg
          :src="firstImg"
          min-width="325"
          min-height="300"
          class="mt-4"
        />
        <div class="w-75">
          <VBtn
            class="BUTTON mt-6 "
            variant="flat"
            color="#BB1F1B"
            @click="changeType('First')"
            block
          >
            <p class="text-capitalize text-white text-subtitle-1">Выбрать</p>
          </VBtn>
        </div>
      </VCol>
      <VCol
        cols="4"
        class="d-flex flex-column align-center"
      >
        <p class="text-h6">Вторичный прием</p>
        <VImg
          :src="secondImg"
          min-width="325"
          min-height="300"
          class="mt-4"
        />
        <div class="w-75">
          <VBtn
            class="BUTTON mt-6 "
            variant="flat"
            color="#BB1F1B"
            @click="changeType('Second')"
            block
          >
            <p class="text-capitalize text-white text-subtitle-1">Выбрать</p>
          </VBtn>
        </div>
      </VCol>
      <VCol
        cols="4"
        class="d-flex flex-column align-center"
      >
        <p class="text-h6">Обучение</p>
        <VImg
          :src="thirdImg"
          min-width="325"
          min-height="300"
          class="mt-4"
        />
        <div class="w-75">
          <VBtn
            class="BUTTON mt-6 "
            variant="flat"
            color="#BB1F1B"
            @click="changeType('Learn')"
            block
          >
            <p class="text-capitalize text-white text-subtitle-1">Выбрать</p>
          </VBtn>
        </div>
      </VCol>
    </VRow>
  </VContainer>
</template>

<script setup lang="ts">
import types from '@samk-dev/nuxt-vcalendar'
import firstImg from 'images/first-priem.svg'
import secondImg from 'images/second-priem.svg'
import thirdImg from 'images/third-priem.svg'
definePageMeta({
  layout: 'forms'
})

const typesPriem = {
  First: {
    name: "Первичный",
  },
  Second: {
    name: "Вторичный",
  },
  Learn: {
    name: "Обучение",
  }
}

const selType = ref()
function changeType(tp) {
  // Получаем массив ключей объекта `cities`
  const typeKeys = Object.keys(typesPriem)
  // Перебираем массив ключей
  for (const typeKey of typeKeys) {
    // Находим город, соответствующий адресу
    if (typeKey === tp) {
      // Инициализируем переменную `selCity`
      selType.value = typesPriem[typeKey].name
      // Возвращаем значение переменной `selCity` из функции `alert()`
    }
  }
}

const savedType = ref()


</script>
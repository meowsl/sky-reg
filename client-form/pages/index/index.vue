<template>
  <VContainer
    class="d-flex justify-top flex-column pb-16"
    style="border: 2px solid black !important; width: 75%; height: 80%;"
  >
    <p
      class="text-h5 font-weight-bold text-center mt-6"
      style="color: #BB1F1B !important"
    >Записаться на прием</p>
    <VRow class="mt-6">
      <VCol
        cols="4"
        class="d-flex flex-column justify-center align-center"
      >
        <p class="text-h6 text-black">Первичный прием</p>
        <VImg
          :src="firstImg"
          width="325"
          height="300"
          class="mt-6"
        />
        <div class="px-8 w-100 mt-8">
          <VBtn
            block="true"
            variant="flat"
            color="#BB1F1B"
            @click="changeType('Первичный')"
          >
            <p class="text-h6 text-white text-capitalize">Выбрать</p>
          </VBtn>
        </div>
      </VCol>
      <VCol
        cols="4"
        class="d-flex flex-column justify-center align-center"
      >
        <p class="text-h6 text-black">Вторичный прием</p>
        <VImg
          :src="secondImg"
          width="325"
          height="300"
          class="mt-6"
        />
        <div class="px-8 w-100 mt-8">
          <VBtn
            block="true"
            variant="flat"
            color="#BB1F1B"
            @click="changeType('Вторичный')"
          >
            <p class="text-h6 text-white text-capitalize">Выбрать</p>
          </VBtn>
        </div>
      </VCol>
      <VCol
        cols="4"
        class="d-flex flex-column justify-center align-center"
      >
        <p class="text-h6 text-black">Обучение</p>
        <VImg
          :src="learnImg"
          width="325"
          height="300"
          class="mt-6"
        />
        <div class="px-8 w-100 mt-8">
          <VBtn
            block="true"
            variant="flat"
            color="#BB1F1B"
            @click="changeType('Обучение')"
          >
            <p class="text-h6 text-white text-capitalize">Выбрать</p>
          </VBtn>
        </div>
      </VCol>
    </VRow>
  </VContainer>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Applications } from '../models/applications'
import firstImg from 'images/firstImg.svg'
import secondImg from 'images/secondImg.svg'
import learnImg from 'images/learnImg.svg'

const router = useRouter()
const selType = ref()

function changeType(tp) {
  selType.value = tp
  const dataList = []
  dataList.push(selType.value)
  router.push({
    path: '/address-form',
    query: {
      data: dataList,
    }
  })
}
</script>


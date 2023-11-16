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
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import backArrow from 'images/backArrow.svg'
import { VForm } from 'vuetify/lib/components'

const router = useRouter()

const fuckingType = ref()
fuckingType.value = router.currentRoute.value.query.type

const fuckingCity = ref()
fuckingCity.value = router.currentRoute.value.query.city

const fuckingDate = ref()
fuckingDate.value = router.currentRoute.value.query.date

const fuckingTime = ref()
fuckingTime.value = router.currentRoute.value.query.time


</script>
<template>
  <div class="address-line d-flex flex-row mt-3">
    <NuxtLink to="/schedule-page">
      <VBtn
        icon
        variant="outlined"
        width="35"
        height="35"
        class="back-btn d-flex justify-center align-center"
      >
        <VImg
          :src="iconBack"
          min-width="25"
          min-height="25"
        />
      </VBtn>
    </NuxtLink>
    <p class="text-h5">Адрес: {{ $route.query.physAddress }} / </p>
    <p class="text-h5">Дата: {{ $route.query.formattedDate }}</p>
  </div>

  <div class="cabinets mt-5 d-flex justify-center">
    <div class="cabinet-item d-flex justify-space-between w-50">
      <div
        v-for="cab in cabList"
        :key="cab.id"
      >
        <VHover>
          <template v-slot:default="{ isHovering, props }">
            <VBtn
              variant="text"
              icon
              v-bind="props"
              class="d-flex flex-column text-capitalize text-capitalize"
            >
              <NuxtLink to="/cabinets-page">
                <VImg
                  :src="isHovering ? cabinetOpen : icon"
                  width="60"
                  class="mx-auto"
                />
                <p class="text-black">Кабинет {{ cab?.cabinetNum }}</p>
              </NuxtLink>
            </VBtn>
          </template>
        </VHover>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import icon from 'images/icon-cabinet-close.svg'
import cabinetOpen from 'images/icon-cabinet-open.svg'
import iconBack from 'images/icon-back.svg'
import { Cabinets } from 'models/cabinets'
import { ref } from 'vue'

const { $api } = useNuxtApp()
const cabList = ref<Cabinets[]>([])

const getCabs = async () => {
  cabList.value = await $api<Cabinets[]>('skyreg/cabinets/')
}
getCabs()

const formattedDateProp = defineProps(['formattedDateProp'])

</script>
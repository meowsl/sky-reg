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
    <div class="d-flex flex-row justify-start">
      <p class="text-h6 ms-2">Адрес: {{ $route.query.physAddress }} \/ </p>
      <p class="text-h6 ms-2">Дата: {{ $route.query.formattedDate }}</p>
    </div>
  </div>

  <div class="cabinets mt-10 d-flex justify-center">
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
              <div class="d-flex flex-column">
                <VImg
                  :src="isHovering ? cabinetOpen : icon"
                  width="60"
                  class="mx-auto"
                />
                <p class="text-black">Кабинет {{ cab?.cabinetNum }}</p>
              </div>
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

const names = {
  Ростов: {
    name: "rostov"
  },
  Краснодар: {
    name: "krasnodar"
  },
  Сочи: {
    name: "sochi"
  }
}

const router = useRouter()
const savedPhys = ref()
const addrForApi = ref()

savedPhys.value = router.currentRoute.value.query.physAddress

// Получение url для api
const nameKeys = Object.keys(names)
for (const nameKey of nameKeys) {
  if (nameKey === savedPhys.value.split(',')[0]) {
    addrForApi.value = names[nameKey].name
  }
}
const strapi = `/${addrForApi.value}-cabinets`

// Получение кабинетов
const { $api } = useNuxtApp()
const cabList = ref<Cabinets[]>([])

const getCabs = async () => {
  cabList.value = await $api<Cabinets[]>(`skyreg${strapi}`)
}
getCabs()


</script>
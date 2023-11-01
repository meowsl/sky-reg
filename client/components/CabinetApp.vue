<template>
  <div class="cabinets mt-5 d-flex justify-center">
    <div class="cabinet-item d-flex justify-space-between w-50">
      <h1>{{ $route.query.formattedDate }}</h1>
      <div
        v-for="cab in cabList"
        :key="cab.id"
      >
        <VHover>
          <template v-slot:default="{ isHovering, props }">
            <NuxtLink
              to="/cabinets-page"
              v-bind="props"
            >
              <VImg
                :src="isHovering ? cabinetOpen : icon"
                width="60"
                class="mx-auto"
              />
              <p>Кабинет {{ cab?.cabinetNum }}</p>
            </NuxtLink>
          </template>
        </VHover>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import icon from 'images/icon-cabinet-close.svg'
import cabinetOpen from 'images/icon-cabinet-open.svg'
import { Cabinets } from 'models/cabinets'
import { ref, provide } from 'vue'

const { $api } = useNuxtApp()
const cabList = ref<Cabinets[]>([])



const getCabs = async () => {
  cabList.value = await $api<Cabinets[]>('skyreg/cabinets/')
}
getCabs()

const { formattedDateProp } = defineProps(['formattedDateProp'])
console.log(formattedDateProp)
</script>
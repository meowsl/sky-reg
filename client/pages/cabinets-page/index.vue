<template>
  <div class="cabinets-page">
    <p class="text-h4 font-weight-bold">Кабинеты</p>
    <div
      v-for="cab in filteredCabs"
      :key="cab.id"
    >
      <p class="text-black">Город {{ cab?.city }} Номер кабинета {{ cab?.num }}</p>

    </div>
  </div>
</template>

<script lang="ts" setup>
import { Cabinets } from 'models/cabinets'
import { ref } from 'vue'
const { $api } = useNuxtApp()
const cabList = ref<Cabinets[]>([])
const getCabs = async () => {
  cabList.value = await $api<Cabinets[]>(`/skyreg/cabinets/list/`)
}
getCabs()

const filteredCabs = ref<Cabinets[]>([])
watchEffect(() => {
  // Фильтруем кабинеты по city=
  filteredCabs.value = cabList.value.filter(cab => cab.city.toString() === 'Ростов-на-Дону')
})
</script>
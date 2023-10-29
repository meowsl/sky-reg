<template>
  <VTable
    fixed-header
    height="300px"
    theme="white"
  >
    <thead>
      <tr>
        <th class="text-left ps-0">
          №

        </th>

        <th class="text-left ps-0">
          Дата обращения
        </th>
        <th class="text-left ps-0">
          Номер
        </th>
        <th class="text-left ps-0">
          ФИО
        </th>
        <th class="text-left ps-0">
          Тип приема
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="app in appsList"
        :key="app.id"
      >
        <td class="ps-0">{{ app?.id }}</td>
        <td class="ps-0">{{ app?.dateApplication }}</td>
        <td class="ps-0">{{ app?.phone }}</td>
        <td class="ps-0">{{ app?.lastName }} {{ app?.firstName }} {{ app?.middleName }}</td>
        <td class="ps-0">{{ app?.typePriem }}</td>
      </tr>
    </tbody>

  </VTable>
</template>

<script setup lang="ts">
import { Applications } from 'models/applications'
const { $api } = useNuxtApp()
const appsList = ref<Applications[]>([])
const getApps = async () => {
  appsList.value = await $api<Applications[]>('skyreg/applications/')
}
getApps()
</script>
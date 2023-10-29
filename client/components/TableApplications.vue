<template>
  <VTable
    fixed-header
    height="300px"
    theme="white"
  >
    <thead>
      <tr>
        <th class="text-left">
          №

        </th>

        <th class="text-left">
          Дата обращения
        </th>
        <th class="text-left">
          Номер
        </th>
        <th class="text-left">
          ФИО
        </th>
        <th class="text-left">
          Тип приема
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="app in appsList"
        :key="app.id"
      >
        <td>{{ app?.id }}</td>
        <td>{{ app?.dateApplication }}</td>
        <td>{{ app?.phone }}</td>
        <td>{{ app?.lastName }} {{ app?.firstName }} {{ app?.middleName }}</td>
        <td>{{ app?.typePriem }}</td>
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
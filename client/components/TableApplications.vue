<template>
  <div class="search d-flex justify-end align-end py-4">
    <VMenu>
      <template v-slot:activator="{ props }">
        <v-btn
          v-bind="props"
          color="black"
          class="px-2"
          icon
        >
          <VImg
            :src="filter"
            width="30"
            height="30"
          />
        </v-btn>
      </template>

      <VCard
        width="300"
        class="pa-4"
      >

      </VCard>
    </VMenu>
  </div>
  <VTable
    class="table"
    fixed-header
    height="300px"
  >

    <thead>
      <tr>
        <th class="table__text-left ps-0 w-auto">
          №
        </th>
        <th class="table__text-left text-center ps-0">
          Дата записи
        </th>
        <th class="table__text-left text-center ps-0">
          Время
        </th>
        <th class="table__text-left text-center ps-0">
          Номер
        </th>
        <th class="table__text-left text-center ps-0">
          ФИО
        </th>
        <th class="table__text-left text-center ps-0">
          Тип приема
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="app in list"
        :key="app.id"
        class=""
      >
        <td class="ps-0">{{ app?.id }}</td>
        <td class="ps-0 text-center">{{ app?.date }}</td>
        <td class="ps-0 text-center">{{ app?.time }}</td>
        <td class="ps-0 text-center">{{ app?.phone }}</td>
        <td class="ps-0 text-center">{{ app?.lastname }} {{ app?.firstname }}</td>
        <td class="ps-0 text-center">{{ app?.typepr }}</td>
      </tr>
    </tbody>

  </VTable>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Applications } from 'models/applications'
import { useAppoints } from '../composables'

import filter from 'images/icon-filter.svg'
import calendar from 'images/icon-calendar.svg'

const { getApps, filteredDate, filteredType } = useAppoints()

let list = ref<Applications[]>([])

onMounted(async () => {
  list.value = await getApps()
})

</script>
<template>
  <VTable
    class="table"
    fixed-header
    height="300px"
  >
    <thead>
      <tr>
        <th class="table__text-left ps-0">
          №
        </th>
        <th class="table__text-left ps-0">
          Дата записи
        </th>
        <th class="table__text-left ps-0">
          Время
        </th>
        <th class="table__text-left ps-0">
          Номер
        </th>
        <th class="table__text-left ps-0">
          ФИО
        </th>
        <th class="table__text-left ps-0">
          Тип приема
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="app in appsList"
        :key="app.id"
        class=""
      >
        <td class="ps-0">{{ app?.id }}</td>
        <td class="ps-0">{{ app?.date }}</td>
        <td class="ps-0">{{ app?.time }}</td>
        <td class="ps-0">{{ app?.phone }}</td>
        <td class="ps-0">{{ app?.lastname }} {{ app?.firstname }}</td>
        <td class="ps-0">{{ app?.typepr }}</td>
      </tr>
    </tbody>

  </VTable>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Applications } from 'models/applications'
import Arrow from 'images/icon-doc.svg'
const router = useRouter()
const { $api } = useNuxtApp()

const appsList = ref<Applications[]>([])
const getApps = async () => {
  appsList.value = await $api<Applications[]>('personals/applications/list/')
  console.log(appsList.value)
  // alert(JSON.stringify(appsList.value[0]['id']))
}
getApps()

</script>
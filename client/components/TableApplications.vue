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
          Дата обращения
        </th>
        <th class="table__text-left ps-0">
          Дата записи
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
        <td class="ps-0">{{ app?.dateApplication }}</td>
        <td class="ps-0">{{ app?.dateApplication }}</td>
        <td class="ps-0">{{ app?.phone }}</td>
        <td class="ps-0">{{ app?.lastName }} {{ app?.firstName }} {{ app?.middleName }}</td>
        <td class="ps-0">{{ app?.typePriem }}</td>
        <VBtn
          variant="outline"
          icon
          @click="getData(app?.id)"
        >
          <VImg
            :src="Arrow"
            min-width="30"
          />
        </VBtn>
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
  appsList.value = await $api<Applications[]>('personals/applications/')
  // alert(JSON.stringify(appsList.value[0]['id']))
}
getApps()

const selName = ref()
const savedName = ref()

const selType = ref()
const savedType = ref()

function getData(id) {
  selName.value = JSON.stringify(appsList.value[id - 1]['lastName']).replace('"', ' ').replace('"', ' ') + JSON.stringify(appsList.value[id - 1]['firstName']).replace('"', ' ').replace('"', ' ')
  selType.value = JSON.stringify(appsList.value[id - 1]['typePriem']).replace('"', ' ').replace('"', ' ')
  savedName.value = selName.value
  savedType.value = selType.value
  console.log(savedName.value)
  router.push({
    path: '/city-page',
    query: {
      fio: savedName.value,
      typePriem: savedType.value
    },
  })
}

</script>
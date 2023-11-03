<template>
  <div class="address-line d-flex flex-row align-center mt-3">
    <NuxtLink to="/city-page">
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
      <p class="text-h6 ms-2 text-green font-weight-bold">Дата: {{ formattedDate }}</p>
    </div>
  </div>
  <div class="schedule-page">
    <div class="mt-6 d-flex flex-column justify-center align-center">
      <client-only>
        <VDatePicker
          :select-attribute="selectAttribute"
          :attributes="attrs"
          :min-date="new Date()"
          trim-weeks
          class="vc"
          v-model="date"
          is-required
          :masks="{ weekdays: 'WW' }"
        />
        <h1></h1>
      </client-only>

      <VBtn
        variant="tonal"
        color="green"
        @click="saveDate"
        class="text-capitalize"
      >
        <p class="text-black">Подтвердить</p>
      </VBtn>

    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import iconBack from 'images/icon-back.svg'


const date = ref(new Date()
)
const selectAttribute = ref({
  highlight: {
    color: 'teal',
    fillMode: 'solid'

  }
})
const attrs = ref([
  {
    highlight: {
      color: 'green',
      fillMode: 'solid'
    },
    date: new Date(),

  },
])

const formattedDate = computed(() => {
  const day = date.value.getDate().toString().padStart(2, '0')
  const month = (date.value.getMonth() + 1).toString().padStart(2, '0')
  const year = date.value.getFullYear()
  return `${day}.${month}.${year}`
})

const savedFormattedDate = ref('')
const savedPhys = ref()
const savedFio = ref()
const savedType = ref()
const router = useRouter()

savedPhys.value = router.currentRoute.value.query.physAddress
savedFio.value = router.currentRoute.value.query.fio
savedType.value = router.currentRoute.value.query.typePriem

const saveDate = () => {
  savedFormattedDate.value = formattedDate.value
  // savedPhys.value = router.currentRoute.value.query.physAddress

  router.push({
    path: '/cabinets-page',
    query: {
      formattedDate: savedFormattedDate.value,
      physAddress: savedPhys.value,
      fio: savedFio.value,
      typePriem: savedType.value
    }
  })
}

</script>
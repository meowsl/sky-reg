<template>
  <VContainer
    class="form d-flex flex-column justify-space-between"
    style="border: 2px solid black !important; width: 75%; height: 80%;"
  >
    <div class="form__content-head px-16">
      <p
        class="form__title text-h5 font-weight-bold text-center py-6"
        style="color: #BB1F1B !important"
      >Записаться на прием</p>
      <VDivider />
    </div>
    <div class="form__content d-flex flex-column justify-start align-center mt-12 h-75">
      <p class="<string>">Выберите дату и время</p>
      <VContainer class="w-100 mt-4 d-flex flex-row justify-space-between align-center">
        <VRow>
          <VCol cols="6">
            <div class="form__content__date-choise d-flex flex-column justify-center align-center px-16">
              <p>Дата</p>
              <VExpansionPanels
                class="mt-4"
                static
                variant="inset"
              >
                <VExpansionPanel :title="formattedDate">
                  <VExpansionPanelText>
                    <VDatePicker
                      :min-date="new Date()"
                      transparent
                      borderless
                      trim-weeks
                      v-model="date"
                      is-required
                      :masks="{ weekdays: 'WW' }"
                    >
                    </VDatePicker>
                  </VExpansionPanelText>
                </VExpansionPanel>
              </VExpansionPanels>
            </div>
          </VCol>
          {{ inputValue }}
          <VCol cols="6">
            <div class="form__content__time-choise d-flex flex-column justify-center align-center w-100 px-16">
              <p>Время</p>
              <VExpansionPanels
                class="mt-4"
                variant="inset"
              >
                <VExpansionPanel :title="selTime">
                  <VExpansionPanelText>
                    <div class=" d-flex flex-row flex-wrap justify-center align-center pa-4">

                      <VBtn
                        variant="tonal"
                        v-for=" item in DepartTime"
                        @click="selTime = item"
                        :disabled="!isTimeSlotAvailable(item)"
                        class="mx-2 my-2"
                        color="#BB1F1B"
                      >{{ item }}</VBtn>
                    </div>
                  </VExpansionPanelText>
                </VExpansionPanel>
              </VExpansionPanels>
            </div>
          </VCol>
        </VRow>
      </VContainer>
      <VBtn
        variant="flat"
        color="#BB1F1B"
        height="65"
        class="form-button mt-16 w-25"
        @click="saveDateTime()"
      >
        <p class="text-h5 text-white text-capitalize font-weight-bold">Продолжить</p>
      </VBtn>
    </div>

    <div class="form__content-foot d-flex flex-column justify-center px-16">
      <VDivider />
      <div class="d-flex flex-row justify-start align-center text-start">
        <NuxtLink
          to="/"
          class="d-flex flex-row align-center py-6"
        >
          <VImg
            :src="backArrow"
            width="40"
            height="40"
          />
          <p class="ms-4 text-h6">Назад</p>
        </NuxtLink>
      </div>
    </div>
  </VContainer>
</template>

<script setup lang="ts">
import { ref, computed, watchEffect } from 'vue'
import { useRouter } from 'vue-router'
import backArrow from 'images/backArrow.svg'
import { Schedules } from 'models/schedules'

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

const { $api } = useNuxtApp()
const router = useRouter()
const scheduleList = ref<Schedules[]>([])

const savedType = ref()
const savedAddr = ref()

savedType.value = router.currentRoute.value.query.type
savedAddr.value = router.currentRoute.value.query.city

const date = ref(new Date())
const selTime = ref('10:00')
const formattedDate = computed(() => {
  const day = date.value.getDate().toString().padStart(2, '0')
  const month = (date.value.getMonth() + 1).toString().padStart(2, '0')
  const year = date.value.getFullYear()
  return `${day}.${month}.${year}`
})


const addrForApi = ref()
const nameKeys = Object.keys(names)
for (const nameKey of nameKeys) {
  if (nameKey === savedAddr.value) {
    addrForApi.value = names[nameKey].name
  }
}

const checkAvailability = async () => {
  try {
    scheduleList.value = await $api<Schedules[]>(`/skyreg/schedule/${addrForApi.value}`)
  } catch (error) {
    console.error('Ошибка при получении данных', error)
  }
}

const isTimeSlotAvailable = (time: string): boolean => {
  const busyTimes = scheduleList.value
    .filter(entry => entry.date === formattedDate.value)
    .map(entry => entry.time)
  return !busyTimes.includes(time)
}

watchEffect(() => {
  checkAvailability()
})

let DepartTime: any[] = []
for (let i = 20; i <= 37; i++) {
  let hour = Math.floor(i / 2)
  let minute = (i % 2 === 0) ? '00' : '30'
  if (hour < 10 || (hour === 19 && minute === '30')) continue
  DepartTime.push(`${hour}:${minute}`)
}

function saveDateTime() {
  router.push({
    path: '/name-form',
    query: {
      type: savedType.value,
      city: savedAddr.value,
      date: formattedDate.value,
      time: selTime.value
    }
  })
}
</script>

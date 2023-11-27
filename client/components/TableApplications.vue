<template>
  <VTable
    class="table mt-10"
    fixed-header
  >
    <thead>
      <tr>
        <th class="table__text-left text-center text-black ps-0">
          №
        </th>
        <th
          class="table__text-left text-center text-black"
          style="width:15% !important"
        >
          Дата записи
          <VMenu :close-on-content-click="false">
            <template v-slot:activator="{ props }">
              <v-btn
                v-bind="props"
                color="black"
                class="px-2"
                icon
                variant="alpha"
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
              class="pa-4 d-flex flex-column justify-center"
            >
              <p>Дата</p>
              <v-text-field
                v-model="formattedDate"
                class="input-date"
                color="teal"
              >
                <VBtn
                  variant="text"
                  color="primary"
                  width="20"
                  height="55"
                  class="input-date__btn me-3"
                  @click="isCalendar = true"
                >
                  <VImg
                    :src="calendar"
                    width="30"
                    height="30"
                  />
                </VBtn>
              </v-text-field>
              <VBtn
                variant="flat"
                class="mx-8"
                position="sticky"
                color="teal"
                @click="closeFilterDate()"
              >
                <p class="mx-2 text-subitle-1 text-white text-capitalize">Сбросить</p>
              </VBtn>
            </VCard>
          </VMenu>
        </th>
        <th class="table__text-left text-center text-black ps-0">
          Время
        </th>
        <th class="table__text-left text-center text-black ps-0">
          Номер
        </th>
        <th class="table__text-left text-center text-black ps-0">
          ФИО
        </th>
        <th class="table__text-left text-black text-center">
          Тип приема
          <VMenu :close-on-content-click="false">
            <template v-slot:activator="{ props }">
              <v-btn
                v-bind="props"
                color="black"
                class="px-2"
                icon
                variant="alpha"
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
              class="pa-4 d-flex flex-column justify-center"
            >
              <p>Тип приема</p>
              <v-select
                v-model="typepr"
                :items="typelist"
                persistent-hint
                return-object
                single-line
              ></v-select>
              <VBtn
                variant="flat"
                class="mx-8"
                position="sticky"
                color="teal"
                @click="closeFilterType()"
              >
                <p class="mx-2 text-subitle-1 text-white text-capitalize">Сбросить</p>
              </VBtn>
            </VCard>
          </VMenu>
        </th>
        <th class="table__text-left text-center text-black ps-0">
          Город
          <VMenu :close-on-content-click="false">
            <template v-slot:activator="{ props }">
              <v-btn
                v-bind="props"
                color="black"
                class="px-2"
                icon
                variant="alpha"
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
              class="pa-4 d-flex flex-column justify-center"
            >
              <p>Город</p>
              <v-select
                v-model="city"
                :items="cityList"
                persistent-hint
                return-object
                single-line
              ></v-select>
              <VBtn
                variant="flat"
                class="mx-8"
                position="sticky"
                color="teal"
                @click="closeFilterCity()"
              >
                <p class="mx-2 text-subitle-1 text-white text-capitalize">Сбросить</p>
              </VBtn>
            </VCard>
          </VMenu>
        </th>
        <th class="table__text-left without text-center text-black ps-0">
          Посещение
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="app in schedule"
        :key="app.id"
        :class="`type-` + app?.visit"
      >
        <td class="table__item text-center ps-0">{{ app?.id }}</td>
        <td class="table__item ps-0 text-center">{{ app?.date }}</td>
        <td class="table__item ps-0 text-center">{{ app?.time }}</td>
        <td class="table__item ps-0 text-center">{{ app?.phone }}</td>
        <td class="table__item ps-0 text-center">{{ app?.lastname }} {{ app?.firstname }} {{ app?.midname }} </td>
        <td class="table__item ps-0 text-center">{{ app?.typepr }}</td>
        <td class="table__item ps-0 text-center">{{ app?.city }}</td>
        <td class="ps-0 text-center">
          <VBtn
            class="text-h5 "
            icon="mdi mdi-account-cancel-outline"
            color="black"
            variant="text"
            size="40"
            @click="resetVisit(app?.id, 2, app?.firstname, app?.lastname)"
          />
          <VBtn
            class="text-h5 ms-4"
            icon="mdi mdi-account-check-outline"
            color="black"
            variant="text"
            size="40"
            @click="resetVisit(app?.id, 1, app?.firstname, app?.lastname)"
          />
        </td>
      </tr>
    </tbody>
  </VTable>
  <VDialog
    v-model="isCalendar"
    width="auto"
  >
    <VCard
      max-width="940"
      max-height="664"
      class="pa-8 d-flex flex-column align-center"
    >
      <VDatePicker
        transparent
        borderless
        trim-weeks
        v-model="date"
        is-required
        :masks="{ weekdays: 'WW', data: 'DD-MM-YYYY' }"
      />э
      <VBtn
        variant="flat"
        class="mt-4"
        position="sticky"
        color="teal-lighten-1"
        @click="isCalendar = false"
      >
        <p class="mx-2 text-subitle-1 text-white text-capitalize">Применить</p>
      </VBtn>
    </VCard>
  </VDialog>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { Applications } from 'models/applications'
import { useAppoints } from '../composables'
import filter from 'images/icon-filter.svg'
import calendar from 'images/icon-calendar.svg'

const { getApps, filteredDate, filteredType, filteredCity, putVisit } = useAppoints()

const isCalendar = ref(false)

const list = ref<Applications[]>([])
const schedule = ref<Applications[]>([])
const date = ref(new Date)

// Форматирование выбранной даты
const formattedDate = computed(() => {
  const day = date.value.getDate().toString().padStart(2, '0')
  const month = (date.value.getMonth() + 1).toString().padStart(2, '0')
  const year = date.value.getFullYear()
  return `${day}.${month}.${year}`
})

const typepr = ref('')
const typelist = ['Первичный', 'Вторичный', 'Обучение']
const city = ref('')
const cityList = ['Ростов-на-Дону', 'Краснодар', 'Сочи']

// Отслеживание изменений фильтра по типу приема
watch(typepr, newtype => {
  if (!newtype) return
  fType(newtype)
})

// Отслеживание изменений фильтра по дате
watch(formattedDate, newFormatDate => {
  if (!newFormatDate) return
  fDate(newFormatDate)
})

// Отслеживание изменений фильтра по городу
watch(city, newCity => {
  if (!newCity) return
  fCity(newCity)
})

// Функция загрузки данных с api с фильтром по типу приема
const fType = async (type: string) => {
  list.value = await filteredType(type)
  schedule.value = list.value
}

const fDate = async (date: string) => {
  list.value = await filteredDate(date)
  schedule.value = list.value
}

const fCity = async (city: string) => {
  list.value = await filteredCity(city)
  schedule.value = list.value
}

// Загрузка данных с api
onMounted(async () => {
  list.value = await getApps()
  schedule.value = list.value
})

// Функция для сброса фильтра по типу приема
async function closeFilterType() {
  typepr.value = ''
  list.value = await getApps()
  schedule.value = list.value
  return schedule.value
}
// Функция для сброса фильтра по дате
async function closeFilterDate() {
  typepr.value = ''
  list.value = await getApps()
  schedule.value = list.value
  return schedule.value
}

// Функция для сброса фильтра по городу
async function closeFilterCity() {
  city.value = ''
  list.value = await getApps()
  schedule.value = list.value
  return schedule.value
}

const resetVisit = async (id: string | number, visit: number, firstname: string, lastname: string) => {
  try {
    putVisit(id, visit, firstname, lastname)
  } catch (e) {
    console.log(e)
  }
}
</script>
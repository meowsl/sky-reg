<template>
  <VContainer class="create-form d-flex justify-center align-center">
    <VCard class="w-75 pa-8">
      <p class="appointment-page__title text-h4 font-weight-bold text-center pb-8">Создать новую запись</p>
      <v-form
        fast-fail
        validate-on="submit lazy"
        class="form d-flex flex-column justify-center align-center"
        @submit.prevent="handleSubmit"
      >
        <VRow class="">
          <VCol
            cols="4"
            class="form__col"
          >
            <p class="">Имя</p>
            <v-text-field
              v-model="state.firstname"
              placeholder="Иван"
              :error-messages="v$.firstname.$errors.map(e => e.$message)"
              color="teal"
            ></v-text-field>
          </VCol>
          <VCol
            cols="4"
            class="form__col"
          >
            <p class="">Фамилия</p>
            <v-text-field
              v-model="state.lastname"
              placeholder="Иванов"
              :error-messages="v$.lastname.$errors.map(e => e.$message)"
              color="teal"
            ></v-text-field>
          </VCol>
          <VCol
            cols="4"
            class="form__col"
          >
            <p class="">Отчество (необязательно)</p>
            <v-text-field
              v-model="midname"
              placeholder="Иванович"
              color="teal"
            ></v-text-field>
          </VCol>
          <VCol
            cols="4"
            class="form__col"
          >
            <p>Контактный телефон</p>
            <v-text-field
              v-model="state.phone"
              placeholder="+7(123)456-78-90"
              :error-messages="v$.phone.$errors.map(e => e.$message)"
              color="teal"
            ></v-text-field>
          </VCol>
          <VCol
            cols="4"
            class="form__col"
          >
            <p>Город</p>
            <v-select
              v-model="city"
              :items="cityList"
              persistent-hint
              return-object
              single-line
              color="teal"
            ></v-select>
          </VCol>
          <VCol
            cols="4"
            class="form__col"
          >
            <p>Дата записи</p>
            <v-text-field
              v-model="formattedDate"
              :placeholder="formattedDate"
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
          </VCol>
          <VCol
            cols="4"
            class="form__col"
          >
            <p>Время записи</p>
            <v-select
              v-model="time"
              :items="timeRange"
              persistent-hint
              return-object
              single-line
              color="teal"
            ></v-select>
          </VCol>
          <VCol
            cols="4"
            class="form__col"
          >
            <p>Вид приема</p>
            <VSelect
              v-model="typepr"
              :items="typelist"
              persistent-hint
              return-object
              single-line
              color="teal"
            >
            </VSelect>
          </VCol>
          <VCol
            cols="4"
            class="mx-auto"
          >
            <v-switch
              v-model="isClient"
              hide-details
              inset
              label="Посещали ранее?"
              color="teal"
              class="ps-3 w-auto"
            ></v-switch>
          </VCol>
          <VCol cols="4">

          </VCol>
        </VRow>
        <v-btn
          type="submit"
          @click="takeSucces"
          variant="flat"
          color="teal-lighten-1"
          class="mt-8"
        >
          <p class="">Подтвердить запись</p>
        </v-btn>
      </v-form>
    </VCard>
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
          :min-date="new Date()"
          transparent
          borderless
          trim-weeks
          v-model="date"
          is-required
          :masks="{ weekdays: 'WW' }"
        />
        <VBtn
          variant="outlined"
          class="mt-4"
          position="sticky"
          color="black"
          @click="isCalendar = false"
        >
          <p class="mx-2 text-subitle-1 text-black text-capitalize">Закрыть</p>
        </VBtn>
      </VCard>
    </VDialog>
    <v-snackbar
      v-model="isSuccess"
      :timeout="2000"
      color="green-darken-1"
      rounded="pill"
    >
      <p>Запись успешно создана!</p>
    </v-snackbar>
  </VContainer>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useVuelidate } from '@vuelidate/core'
import { required, helpers, numeric } from '@vuelidate/validators'
import { useAppoints } from '../composables'
import { api } from '../boot/axios'

import calendar from 'images/icon-calendar.svg'

// Переменные для выбора даты
const date = ref(new Date)
const time = ref('10:00')
// Переменная для выбора карточки клиента (в разработке)
const isClient = ref(false)
// Переменные для v-model
const midname = ref('')
const isCalendar = ref(false)
const typelist = ['Первичный', 'Вторичный', 'Обучение']
const typepr = ref('Первичный')
const isSuccess = ref(false)
const city = ref<string>('Ростов-на-Дону')
const cityList = ['Ростов-на-Дону', 'Краснодар', 'Сочи']

const { filteredCityDate, createForm } = useAppoints()

// Форматироварие даты
const formattedDate = computed(() => {
  const day = date.value.getDate().toString().padStart(2, '0')
  const month = (date.value.getMonth() + 1).toString().padStart(2, '0')
  const year = date.value.getFullYear()
  return `${day}.${month}.${year}`
})

// Переменные для инпутов
const initialState = {
  firstname: '',
  lastname: '',
  phone: '',
}
const state = reactive({
  ...initialState,
})
const rules = {
  firstname: { required: helpers.withMessage('Это обязательное поле', required) },
  lastname: { required: helpers.withMessage('Это обязательное поле', required) },
  phone: { required: helpers.withMessage('Это обязательное поле', required) },
}
const v$ = useVuelidate(rules, state)

const timeRange = ref([]) // Make 'timeRange' a reactive property

const getTimes = async (city: string, date: string) => {
  const data = await filteredCityDate(city, date)
  const disabledDate = []
  for (const item of data) {
    disabledDate.push(item['time'])
  }
  timeRange.value = [] // Clear the reactive array
  for (let i = 20; i <= 37; i++) {
    let hour = Math.floor(i / 2)
    let minute = (i % 2 === 0) ? '00' : '30'
    if (hour < 10 || (hour === 19 && minute === '30')) continue
    if (disabledDate.includes(`${hour}:${minute}`)) continue
    timeRange.value.push(`${hour}:${minute}`) // Push time slots to the reactive array
  }
}

watch([city, formattedDate], ([newCity, newDate]) => {
  if (!newCity || !newDate) return
  getTimes(newCity, newDate)
})

onMounted(() => {
  getTimes(city.value, formattedDate.value)
})

const takeSucces = async () => {
  const isFormCorrect = await v$.value.$validate()
  if (isFormCorrect === false)
    return

  isSuccess.value = true
}

const handleSubmit = async () => {
  const isFormCorrect = await v$.value.$validate()

  if (isFormCorrect === false)
    return

  const middNa = midname.value
  const formData = new FormData()

  formData.append('firstname', state.firstname)
  formData.append('lastname', state.lastname)
  formData.append('midname', middNa)
  formData.append('phone', state.phone)
  formData.append('date', formattedDate.value)
  formData.append('time', time.value)
  formData.append('typepr', typepr.value)
  formData.append('city', city.value)
  try {
    await createForm(formData)
    state.firstname = ''
    state.lastname = ''
    midname.value = ''
    state.phone = ''
    date.value = new Date()
    time.value = ''
    typepr.value = ''
    city.value = ''
    isSuccess.value = false
  } catch (error) {
    console.log(error)
  }
}
</script>
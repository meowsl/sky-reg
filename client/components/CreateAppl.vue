<template>
  <VContainer class="create-form d-flex justify-center align-center">
    <VCard class="w-75 pa-8">
      <p class="appointment-page__title text-h4 font-weight-bold text-center pb-8">Создать новую запись</p>
      <v-form
        fast-fail
        validate-on="submit lazy"
        @submit.prevent="handleSubmit"
        class="d-flex flex-column justify-center align-center"
      >
        <VRow class="">
          <VCol
            cols="4"
            class="d-flex flex-column"
          >
            <p class="">Имя</p>
            <v-text-field
              v-model="state.firstname"
              placeholder="Иван"
              :rules="firstNameRules"
              :error-messages="v$.firstname.$errors.map(e => e.$message)"
            ></v-text-field>
          </VCol>
          <VCol cols="4">
            <p class="">Фамилия</p>
            <v-text-field
              v-model="state.lastname"
              placeholder="Иванов"
              :rules="lastNameRules"
              :error-messages="v$.lastname.$errors.map(e => e.$message)"
            ></v-text-field>
          </VCol>
          <VCol cols="4">
            <p class="">Отчество (необязательно)</p>
            <v-text-field
              v-model="midname"
              placeholder="Иванович"
              :rules="midNameRules"
            ></v-text-field>
          </VCol>
          <VCol cols="4">
            <p>Контактный телефон</p>
            <v-text-field
              v-model="state.phone"
              placeholder="+7(123)456-78-90"
              :error-messages="v$.phone.$errors.map(e => e.$message)"
            ></v-text-field>
          </VCol>
          <VCol cols="4">
            <p>Дата записи</p>
            <v-text-field
              v-model="formattedDate"
              :placeholder="formattedDate"
              class="input-date"
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
          <VCol cols="4">
            <p>Время записи</p>
            <v-select
              v-model="time"
              :items="timeRange"
              label="Select"
              persistent-hint
              return-object
              single-line
            ></v-select>
          </VCol>
        </VRow>
        <v-switch
          v-model="isClient"
          hide-details
          inset
          label="Посещали ранее?"
          color="green"
          class="ps-3"
        ></v-switch>
        <v-btn
          type="submit"
          variant="flat"
          color="teal-lighten-1"
          class="mt-8"
          @click="handleSubmit"
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
  </VContainer>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useVuelidate } from '@vuelidate/core'
import { required, helpers, numeric } from '@vuelidate/validators'

import calendar from 'images/icon-calendar.svg'

const { $api } = useNuxtApp()

const date = ref(new Date)
const time = ref('10:00')
const isClient = ref(false)
const midname = ref('')
const isCalendar = ref(false)

let timeRange: any[] = []
for (let i = 20; i <= 37; i++) {
  let hour = Math.floor(i / 2)
  let minute = (i % 2 === 0) ? '00' : '30'
  if (hour < 10 || (hour === 19 && minute === '30')) continue
  timeRange.push(`${hour}:${minute}`)
}

const formattedDate = computed(() => {
  const day = date.value.getDate().toString().padStart(2, '0')
  const month = (date.value.getMonth() + 1).toString().padStart(2, '0')
  const year = date.value.getFullYear()
  return `${day}.${month}.${year}`
})

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
  phone: { required: helpers.withMessage('Это обязательное поле', required), numeric: helpers.withMessage('Пожалуйста, введите действительный номер телефона', numeric) },
}

const v$ = useVuelidate(rules, state)

const handleSubmit = async () => {
  const isFormCorrect = await v$.value.$validate()
  if (isFormCorrect === false)
    return
  const data = {
    firstname: state.firstname,
    lastname: state.lastname,
    phone: state.phone,
    date: formattedDate.value,
    time: time.value,
  }
  await $api('personals/applications/create/', { method: 'POST', body: data })
  v$.value.$reset()
  state.firstname = ''
  state.lastname = ''
  midname.value = ''
  state.phone = ''
  date.value = new Date()
  time.value = ''
}
</script>
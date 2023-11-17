<template>
  <VContainer class="create-form d-flex justify-center align-center">
    <VCard class="w-75 pa-8">
      <p class="appointment-page__title text-h4 font-weight-bold text-center pb-8">Создать новую запись</p>
      <v-form
        fast-fail
        @submit.prevent
        class="d-flex flex-column justify-center align-center"
      >
        <VRow class="">
          <VCol
            cols="4"
            class="d-flex flex-column"
          >
            <p class="">Имя</p>
            <v-text-field
              v-model="firstName"
              placeholder="Иван"
              :rules="firstNameRules"
            ></v-text-field>
          </VCol>
          <VCol cols="4">
            <p class="">Фамилия</p>
            <v-text-field
              v-model="lastName"
              placeholder="Иванов"
              :rules="lastNameRules"
            ></v-text-field>
          </VCol>
          <VCol cols="4">
            <p class="">Отчество (необязательно)</p>
            <v-text-field
              v-model="middleName"
              placeholder="Иванович"
              :rules="midNameRules"
            ></v-text-field>
          </VCol>
          <VCol cols="4">
            <p>Контактный телефон</p>
            <v-text-field
              v-model="phone"
              placeholder="+7(123)456-78-90"
            ></v-text-field>
          </VCol>
          <VCol cols="4">
            <p>Дата записи</p>
            <v-text-field
              v-model="selDate"
              :placeholder="formattedDate"
            ></v-text-field>
          </VCol>
          <VCol cols="4">
            <p>Время записи</p>
            <v-text-field
              v-model="selTime"
              :placeholder="time"
            ></v-text-field>
          </VCol>
          <v-switch
            v-model="isClient"
            hide-details
            inset
            label="Посещали ранее?"
            color="green"
            class="ps-3"
          ></v-switch>
        </VRow>
        <v-btn
          type="submit"
          variant="flat"
          color="teal-lighten-1"
          class="mt-2"
        >
          <p class="">Подтвердить запись</p>
        </v-btn>
      </v-form>
    </VCard>
  </VContainer>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const date = ref(new Date)
const time = ref('10:30')
const isClient = ref(false)

const formattedDate = computed(() => {
  const day = date.value.getDate().toString().padStart(2, '0')
  const month = (date.value.getMonth() + 1).toString().padStart(2, '0')
  const year = date.value.getFullYear()
  return `${day}.${month}.${year}`
})
</script>
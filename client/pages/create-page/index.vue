<template>
  <div class="appointment-page d-flex mt-3 flex-column">

    <VContainer class="create-form d-flex justify-center align-center">
      <VCard class="w-75 pa-8">
        <p class="appointment-page__title text-h4 font-weight-bold text-center pb-8">Создать новую запись</p>
        <v-form
          fast-fail
          @submit.prevent
        >
          <VRow class="">
            <VCol
              cols="4"
              class="d-flex flex-column"
            >
              <p class="">Имя</p>
              <v-text-field
                v-model="firstName"
                label="First name"
                :rules="firstNameRules"
              ></v-text-field>
            </VCol>
            <VCol cols="4">
              <p class="">Фамилия</p>
              <v-text-field
                v-model="lastName"
                label="Last name"
                :rules="lastNameRules"
              ></v-text-field>
            </VCol>
            <VCol cols="4">
              <p class="">Отчество (необязательно)</p>
              <v-text-field
                v-model="middleName"
                label="Last name"
                :rules="midNameRules"
              ></v-text-field>
            </VCol>
            <VCol cols="4">
              <p>Контактный телефон</p>
              <v-text-field
                v-model="phone"
                label="Phone Number"
              ></v-text-field>
            </VCol>
            <VCol cols="4">
              <p>Дата записи</p>
              <v-text-field
                v-model="date"
                label="Дата записи"
              ></v-text-field>
            </VCol>
            <VCol cols="4">
              <p>Время записи</p>
              <v-text-field
                v-model="time"
                label="Время записи"
              ></v-text-field>
            </VCol>
            <v-btn
              type="submit"
              block
              class="mt-2"
            >Submit</v-btn>
          </VRow>
        </v-form>
      </VCard>
    </VContainer>
  </div>
</template>

<script setup lang="ts"></script>
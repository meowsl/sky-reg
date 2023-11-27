<template>
  <VContainer class="login h-screen w-screen d-flex justify-center align-center">
    <VForm
      class="login__form"
      @submit.prevent="onSubmit()"
    >
      <VCard
        class="login__card pa-8 d-flex flex-column"
        width="500"
        elevation="24"
      >
        <v-card-title class="text-center text-h4">Вход в систему</v-card-title>

        <v-card-text class="mt-12">
          <v-text-field
            v-model="login"
            placeholder="Логин"
            required
            color="teal"
            hint="Введите свой логин"
          ></v-text-field>

          <v-text-field
            class="mt-4"
            v-model="password"
            placeholder="Пароль"
            type="password"
            required
            color="teal"
            hint="Введите пароль"
          ></v-text-field>
        </v-card-text>

        <v-card-actions class="d-flex justify-center px-16">
          <v-btn
            class="pa-4 d-flex justify-center align-center"
            variant="flat"
            block
            type="submit"
            color="teal-lighten-1"
          >
            <p class="text-capitalize text-subtitle-1">Войти</p>
          </v-btn>
        </v-card-actions>
      </VCard>
    </VForm>
  </VContainer>
</template>

<script setup lang="ts">
import { ref } from 'vue'

import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()

const login = ref('')
const password = ref('')

const onSubmit = async () => {
  alert('is started')
  try {
    await authStore.userLogin(login.value.toLowerCase(), password.value)
  } catch (error) {
    alert(error)
    console.error(error)
  }
}
</script>
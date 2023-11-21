<template>
  <VContainer class="h-screen w-screen d-flex justify-center align-center">
    <VForm>
      <VCard
        class="pa-16 d-flex flex-column"
        width="500"
      >
        <v-card-title class="text-center text-h4">Вход в систему</v-card-title>

        <v-card-text class="mt-12">
          <v-text-field
            v-model="login"
            label="Логин"
            required
            hint="Введите свой логин"
          ></v-text-field>

          <v-text-field
            v-model="password"
            label="Пароль"
            type="password"
            required
            error="Пароль должен быть не менее 8 символов"
          ></v-text-field>
        </v-card-text>

        <v-card-actions class="d-flex justify-center">
          <v-btn
            color="primary"
            @click="submit"
          >
            Войти
          </v-btn>
        </v-card-actions>
      </VCard>
    </VForm>
  </VContainer>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const login = ref('')
const password = ref()
</script>
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
            v-model="state.login"
            placeholder="Логин"
            required
            color="teal"
            hint="Введите свой логин"
          ></v-text-field>

          <v-text-field
            class="mt-4"
            v-model="state.password"
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
            @click="handleSubmit"
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
import { useVuelidate } from '@vuelidate/core'
import { required, helpers } from '@vuelidate/validators'
import type { AuthState } from 'client/models/auth'

const { $api } = useNuxtApp()
const router = useRouter()

const initialState = {
  login: '',
  password: '',
}

const state = reactive({
  ...initialState,
})

const rules = {
  login: { required: helpers.withMessage('Это обязательное поле', required) },
  password: { required: helpers.withMessage('Это обязательное поле', required) },
}
const v$ = useVuelidate(rules, state)

const handleSubmit = async () => {
  const isFormCorrect = await v$.value.$validate()
  if (!isFormCorrect) {
    return
  } else {
    const data = {
      'username': state.login,
      'password': state.password,
    }
    const response = await $api('/auth/token/', { method: 'POST', body: data })
    try {
      localStorage.setItem('token', response['access'])
      router.push({
        path: '/'
      })
    } catch (error) {
      alert(error)
    }
    v$.value.$reset()
    state.login = ''
    state.password = ''
  }
}
</script>
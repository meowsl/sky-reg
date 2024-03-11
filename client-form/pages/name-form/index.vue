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
    <div class="form__content px-16 d-flex flex-column align-center">
      <p class="form__title text-h6 text-center text-black ">Введите свои данные</p>
      <VForm
        v-model="valid"
        @submit.prevent
        class="px-16 mt-4"
      >
        <VRow class="px-16">
          <v-col
            cols="12"
            class="px-16"
          >
            <v-text-field
              v-model="state.firstName"
              placeholder="Имя"
              :error-messages="v$.firstName.$errors.map(e => e.$message)"
              required
              hide-details
            ></v-text-field>
          </v-col>
          <v-col
            cols="6"
            class="px-16"
          >
            <v-text-field
              v-model="state.lastName"
              placeholder="Фамилия"
              :error-messages="v$.lastName.$errors.map(e => e.$message)"
              hide-details
              required
            ></v-text-field>
          </v-col>
          <v-col
            cols="6"
            class="px-16 "
          >
            <v-text-field
              v-model="state.middleName"
              placeholder="Отчество(необязательно)"
              :error-messages="v$.lastName.$errors.map(e => e.$message)"
              hide-details
              required
            ></v-text-field>
          </v-col>
          <v-col
            cols="12"
            class="px-16"
          >
            <v-text-field
              v-model="state.phone"
              :error-messages="v$.phone.$errors.map(e => e.$message)"
              placeholder="+7(123)456-78-90"
            ></v-text-field>
          </v-col>
        </VRow>
      </VForm>
      <v-snackbar
        :timeout="2000"
        color="green-darken-1"
        rounded="pill"
        height="1200"
      >
        <template v-slot:activator="{ props }">
          <VBtn
            variant="flat"
            color="#BB1F1B"
            height="65"
            class="w-25"
            v-bind="props"
            @click="handleSubmit()"
          >
            <p class="text-h5 text-white text-capitalize font-weight-bold">Подтвердить</p>
          </VBtn>
        </template>

        Ваша заявка успешно отправлена!
      </v-snackbar>
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

<script
  setup
  lang="ts"
>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useVuelidate } from '@vuelidate/core'
import { required, helpers } from '@vuelidate/validators'
import backArrow from 'images/backArrow.svg'

const router = useRouter()

const fuckingType = ref()
fuckingType.value = <string>router.currentRoute.value.query.type
const fuckingCity = ref()
fuckingCity.value = <string>router.currentRoute.value.query.city
const fuckingDate = ref()
fuckingDate.value = <string>router.currentRoute.value.query.date
const fuckingTime = ref()
fuckingTime.value = <string>router.currentRoute.value.query.time

const { $api } = useNuxtApp()

const initialState = {
  firstName: '',
  lastName: '',
  middleName: '',
  phone: '',
}
const state = reactive({
  ...initialState,
})

const rules = {
  firstName: { required: helpers.withMessage('Это обязательное поле', required) },
  lastName: { required: helpers.withMessage('Это обязательное поле', required) },
  phone: { required: helpers.withMessage('Это обязательное поле', required) },
}

const v$ = useVuelidate(rules, state)

const handleSubmit = async () => {
  const isFormCorrect = await v$.value.$validate()

  if (isFormCorrect === false)
    return

  const data = {
    firstname: state.firstName,
    lastname: state.lastName,
    midname: state.middleName,
    phone: state.phone,
    date: fuckingDate.value,
    time: fuckingTime.value,
    typepr: fuckingType.value,
    city: fuckingCity.value
  }
  console.log(data)
  try {
    await $api('personals/applications/create/', { method: 'POST', title: 'title', body: data })
    v$.value.$reset()
    state.firstName = ''
    state.lastName = ''
    state.middleName = ''
    state.phone = ''
    fuckingDate.value = ''
    fuckingTime.value = ''
    fuckingCity.value = ''
  } catch (error) {
    alert(error)
  }
}

</script>
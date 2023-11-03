<template>
  <div class="address-line d-flex flex-row align-center mt-3">
    <div class="d-flex flex-row justify-start">
      <p class="text-h6 ms-2 text-green font-weight-bold">Адрес: {{ selCity }}</p>
    </div>
  </div>
  <div class="d-flex align-center justify-center">
    <VContainer>
      <VRow
        v-model="city"
        class="pa-16   d-flex align-start"
      >
        <VCol
          cols="4"
          class="d-flex flex-column justify-center align-start"
        >
          <div class="city-title d-flex align-center justify-center">
            <p class="text-h6 mt-2">Ростов-на-Дону</p>
          </div>
          <div class="center-address d-flex justify-center align-center my-2">
            <VBtn
              variant="text"
              class="text-capitalize"
              v-on:click="changeCity('Rostov')"
            >
              <p class="text-black">адрес_1</p>
            </VBtn>
          </div>
          <div class="end-address d-flex justify-center align-center">
            <p>В разработке</p>
          </div>
        </VCol>
        <VCol
          cols="4"
          class="d-flex flex-column justify-center align-start"
        >
          <div class="city-title d-flex align-center justify-center">
            <p class="text-h6 mt-2">Краснодар</p>
          </div>
          <div class="end-address d-flex justify-center align-center my-2">
            <VBtn
              variant="text"
              class="text-capitalize"
              v-on:click="changeCity('Krasnodar')"
            >
              <p class="text-black">адрес_2</p>
            </VBtn>
          </div>
        </VCol>
        <VCol
          cols="4"
          class="d-flex flex-column justify-center align-start"
        >
          <div class="city-title d-flex align-center justify-center">
            <p class="text-h6 mt-2">Сочи</p>
          </div>
          <div class="end-address d-flex justify-center align-center my-2">
            <VBtn
              variant="text"
              class="text-capitalize"
              @click="changeCity('Sochi')"
            >
              <p class="text-black">адрес_3</p>
            </VBtn>
          </div>
        </VCol>
      </VRow>
    </VContainer>

  </div>
  <div class="d-flex align-center justify-center">
    <VBtn
      variant="tonal"
      color="green"
      @click="saveDate"
      class="text-capitalize"
    >
      <p class="text-black">Подтвердить</p>
    </VBtn>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const city = ref("Ростов")

const cities = {
  Rostov: {
    name: "Ростов",
    address: "адрес_1"
  },
  Krasnodar: {
    name: "Краснодар",
    address: "адрес_2"
  },
  Sochi: {
    name: "Сочи",
    address: "адрес_3"
  }
}

const selCity = ref(' ')
function changeCity(cit) {
  // Получаем массив ключей объекта `cities`
  const cityKeys = Object.keys(cities)
  // Перебираем массив ключей
  for (const cityKey of cityKeys) {
    // Находим город, соответствующий адресу
    if (cityKey === cit) {
      // Инициализируем переменную `selCity`
      selCity.value = cities[cityKey].name + ', ' + cities[cityKey].address
      // Возвращаем значение переменной `selCity` из функции `alert()`
    }
  }
}

const savedPhysAddress = ref('')
const savedFio = ref()
const savedType = ref()
const router = useRouter()

savedFio.value = router.currentRoute.value.query.fio
savedType.value = router.currentRoute.value.query.typePriem

const saveDate = () => {
  savedPhysAddress.value = selCity.value
  console.log(savedPhysAddress.value)
  router.push({
    path: '/schedule-page',
    query: {
      physAddress: savedPhysAddress.value,
      fio: savedFio.value,
      typePriem: savedType.value,
    },
  })
}


</script>
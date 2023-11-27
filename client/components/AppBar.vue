<template>
  <VAppBar
    elevation="1"
    class="app-bar d-flex justify-center py-2"
    height="100"
  >
    <VContainer class="d-flex flex-row align-center justify-space-between">
      <VRow>
        <VCol
          cols="6"
          class="d-flex flex-row align-center"
        >
          <NuxtLink to="/">
            <VImg
              :src="logo"
              min-width="75"
              class="ma-4"
            />
          </NuxtLink>
          <p class="app-bar__name font-weight-medium">Sky<br>Reg</p>
          <p class="app-bar__description text-h6 ms-6 font-weight-medium">облачная<br>регистратура</p>
        </VCol>
        <VCol
          cols="6"
          class="d-flex align-center justify-end"
        >
          <v-menu :location="bottom">
            <template v-slot:activator="{ props }">
              <v-btn
                color="teal"
                variat="text"
                dark
                icon
                width="65"
                height="65"
                v-bind="props"
              >
                <VImg
                  :src="icon"
                  width="60"
                  height="60"
                />
              </v-btn>
            </template>

            <v-list>
              <v-list-item>
                <VBtn
                  variant="flat"
                  color="teal"
                  @click="logoutFunc"
                >
                  <p class="text-capitalize">Logout</p>
                </VBtn>
              </v-list-item>
            </v-list>
          </v-menu>
        </VCol>
      </VRow>
    </VContainer>
  </VAppBar>
</template>

<script setup lang="ts">
import { useAuthStore } from '../stores/auth'

import logo from 'images/logo.svg'
import icon from 'images/icon-account.svg'

const authStore = useAuthStore()
const router = useRouter()

const kekish = authStore.user

const logoutFunc = async () => {
  // try {
  //   await authStore.userLogout()
  // } catch (e) {
  //   alert(e)
  // }
  localStorage.removeItem('token')
  router.push({ path: '/login' })
}
</script>

<template>
  <VAppBar
    elevation="0"
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
          <NuxtLink to="/">
            <VImg
              :src="icon"
              min-width="60"
            />
          </NuxtLink>
        </VCol>
      </VRow>
    </VContainer>
  </VAppBar>
</template>

<script setup lang="ts">
import logo from 'images/logo.svg'
import icon from 'images/icon-account.svg'
</script>

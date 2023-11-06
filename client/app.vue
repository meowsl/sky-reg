<template>
  <VApp>
    <NuxtLayout :name="layout">
      <NuxtPage />

    </NuxtLayout>
    <div class="d-flex flex-row justify-center">
      <VBtn
        @click="chooseDefault"
        class="w-25"
      >Choose admin</VBtn>
      <VBtn
        @click="chooseCustom"
        class="w-25"
      >Choose client</VBtn>
    </div>
  </VApp>
</template>

<script setup lang="ts">
import favicon from 'images/favicon.ico'
useHead({
  title: 'SKY-REG',
  link: [
    {
      rel: 'icon',
      href: favicon,
    },
  ],
})

const layout = ref("default")

function chooseCustom() {
  layout.value = "client"
}
function chooseDefault() {
  layout.value = "default"
}

</script>
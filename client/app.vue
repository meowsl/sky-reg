<template>
  <VApp>
    <NuxtLayout :name="layout">
      <NuxtPage />

    </NuxtLayout>
    <div class="d-flex flex-row justify-center">
      <VBtn @click="chooseDefault">Choose Admin</VBtn>
      <VBtn @click="chooseForms">Choose Client</VBtn>
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

const router = useRouter()

const chooseDefault = () => {
  layout.value = "default"
  router.push({
    path: '/'
  })
}

const chooseForms = () => {
  layout.value = "forms"
  router.push({
    path: '/forms/'
  })
}
</script>
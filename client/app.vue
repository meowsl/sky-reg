<template>
  <VApp>
    <NuxtLayout :name="layout">
      <NuxtPage />

    </NuxtLayout>
  </VApp>
</template>

<script setup lang="ts">
import favicon from 'images/favicon.ico'
useHead({
  title: 'SKY-REG Admin',
  link: [
    {
      rel: 'icon',
      href: favicon,
    },
  ],
})

const layout = ref("default")

const router = useRouter()

</script>
<template>
  <VApp>
    <NuxtLayout>
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

</script>
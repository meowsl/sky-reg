<template>
  <VApp>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </VApp>
</template>

<script setup lang="ts">
useHead({
  title: 'SKY-REG Client',
  link: [
    {
      rel: 'icon',
      href: '/static/favicon.ico',
    },
  ],
})
</script>

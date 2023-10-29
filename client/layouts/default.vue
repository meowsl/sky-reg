<template>
  <VLayout>
    <AppBar />
    <VLayout class="mt-28">

      <NavBlock />
      <VMain class="px-16 py-6">
        <slot />
      </VMain>
    </VLayout>
  </VLayout>
</template>

<script setup lang="ts">
// import rsueLogo from 'images/rsue_logo.svg'
import NavBlock from './NavBlock.vue'
import AppBar from './AppBar.vue'
</script>

<template>
  <VLayout>
    <AppBar />
    <VLayout class="mt-28 h-auto">

      <NavBlock />
      <VMain class="all-pages px-16 py-6">
        <slot />
      </VMain>
    </VLayout>
  </VLayout>
</template>

<script setup lang="ts">
import NavBlock from '../components/NavBlock.vue'
import AppBar from '../components/AppBar.vue'
</script>

<template>
  <v-card>
    <VNavigationDrawer
      permanent
      location="left"
      border="0"
      class="menu py-8 d-flex flex-column"
    >
      <NuxtLink
        to="/"
        class="bg-white d-flex align-center justify-center  text-h6"
      >
        <p class="nav-text">Заявки</p>
      </NuxtLink>
      <NuxtLink
        to="/"
        class="bg-white d-flex align-center justify-center  text-h6 mt-1"
      >
        <p class="nav-text">Расписание</p>
      </NuxtLink>
    </VNavigationDrawer>
    <v-main style="height: 250px"></v-main>
  </v-card>
</template>

<script setup lang="ts"></script>
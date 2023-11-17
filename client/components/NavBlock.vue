<template>
  <v-card class="menu">
    <VNavigationDrawer
      permanent
      location="left"
      class="menu__block py-8 d-flex flex-column"
    >
      <nav>
        <NuxtLink
          to="/"
          class="bg-white d-flex align-center justify-center  text-h6"
        >
          <p class="nav-text">Записи</p>
        </NuxtLink>
        <!-- <NuxtLink
          to="/city-page"
          class="bg-white d-flex align-center justify-center text-h6 mt-1"
        >
          <p class="nav-text">Расписание</p>
        </NuxtLink> -->
        <NuxtLink
          to="/create-page"
          class="bg-white d-flex align-center justify-center text-h6 mt-1"
        >
          <p class="nav-text">Создать запись</p>
        </NuxtLink>
        <NuxtLink
          to="/cabinets-page"
          class="bg-white d-flex align-center justify-center text-h6 mt-1"
        >
          <p class="nav-text">Кабинеты</p>
        </NuxtLink>
      </nav>
    </VNavigationDrawer>
    <v-main style="height: 250px"></v-main>
  </v-card>
</template>

<script setup lang="ts"></script>
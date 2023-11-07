<template>
  <div class="index">
    <h1>Lorem ipsum dolor sit amet.</h1>
    <div
      v-for="app in appsList"
      :key="app.id"
    >
      <p>{{ app?.firstName }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Applications } from '../models/applications'

const { $api } = useNuxtApp()

const appsList = ref<Applications[]>([])
const getApps = async () => {
  appsList.value = await $api<Applications[]>('personals/applications/')
  // alert(JSON.stringify(appsList.value[0]['id']))
}
getApps()
</script>


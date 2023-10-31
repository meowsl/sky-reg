<template>
  <div class="cabinets mt-5 d-flex justify-center">
    <div class="cabinet-item d-flex justify-space-between w-50">
      <div>
        <VImg
          :src=cabinet
          width="60"
          class="mx-auto"
        ></VImg>
        <P>Кабинет 1</P>
      </div>
      <div>
        <VImg
          :src=cabinet
          width="60"
          class="mx-auto"
        ></VImg>
        <P>Кабинет 2</P>
      </div>
      <div>
        <VImg
          :src=cabinet
          width="60"
          class="mx-auto"
        ></VImg>
        <P>Обучение</P>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import cabinet from 'images/icon-cabinet.png'
</script>
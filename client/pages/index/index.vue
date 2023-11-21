<template>
  <div class="applications-page">
    <p class="text-h4 font-weight-bold">Записи</p>
    <VContainer class="px-16">
      <TableApplications />
    </VContainer>
  </div>
</template>

<script setup lang="ts">

const router = useRouter()

onMounted(async () => {
  const checkAuth = localStorage.getItem('token')
  if (checkAuth == null) {
    router.push({
      path: '/login'
    })
  }
})
</script>

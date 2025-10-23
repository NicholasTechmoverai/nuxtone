<template>
  <div>
    <div v-if="pending">Loading user...</div>
    <div v-else-if="error">User not found</div>
    <div v-else>
      <h1 class="text-2xl font-bold">{{ user.name }}</h1>
      <p>{{ user.email }}</p>
      <p class="text-gray-500 mt-2">Joined: {{ user.created_at }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
const route = useRoute()
const { data: user, pending, error } = await useApi(`/users/${route.params.id}`)
useHead({ title: `${user?.value?.name ?? 'User'} - Profile` })
</script>

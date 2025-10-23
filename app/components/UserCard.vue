<template>
  <div class="border p-4 rounded shadow hover:shadow-lg transition">
    <h2 class="text-lg font-semibold">{{ user.name }}</h2>
    <p class="text-sm text-gray-500">{{ user.email }}</p>
    <NuxtLink :to="`/users/${user.id}`" class="text-blue-600 hover:underline mt-2 block">
      View Profile
    </NuxtLink>
  </div>
</template>

<script setup lang="ts">
defineProps<{ user: { id: string; name: string; email: string } }>()
</script>

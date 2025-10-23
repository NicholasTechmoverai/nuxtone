<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">Users</h1>
    <div v-if="pending">Loading users...</div>
    <div v-else>
      <div class="grid gap-4 sm:grid-cols-2 md:grid-cols-3">
        <UserCard v-for="user in users" :key="user.id" :user="user" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import UserCard from '~/components/UserCard.vue'

interface User {
  id: string
  name: string
  email: string
}

const { data: users, pending } = await useApi<User[]>('/users')
useHead({ title: 'Users - Nuxt + FastAPI Demo' })
</script>

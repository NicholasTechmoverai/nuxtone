<template>
  <div class="min-h-screen p-6 bg-gray-50 dark:bg-gray-800">
    <h1 class="text-3xl font-bold mb-6 text-gray-800">Users Directory</h1>

    <div v-if="users" class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
      <UCard
        v-for="user in users"
        :key="user.id"
        class="hover:shadow-lg transition-shadow"
      >
        <div class="flex items-center gap-4">
          <UAvatar :src="user.avatar" :alt="user.name" size="lg" />
          <div>
            <h3 class="font-semibold text-lg">{{ user.name }}</h3>
            <p class="text-gray-600 text-sm">{{ user.email }}</p>
            <UBadge
              :color="user.role === 'premium' ? 'amber' : 'gray'"
              class="mt-1"
            >
              {{ user.role }}
            </UBadge>
          </div>
        </div>

        <template #footer>
          <NuxtLink
            :to="`/user/${user.id}`"
            class="text-primary font-medium hover:underline"
          >
            View Profile →
          </NuxtLink>
        </template>
      </UCard>
    </div>

    <p v-else class="text-gray-500 text-center">Loading users...</p>
  </div>
</template>

<script setup lang="ts">
import { useApi } from '~/composables/useApi'
import { useSeo } from '~/composables/useSeo'

// Setup SEO for the directory
useSeo('User Directory', 'Browse all user profiles on Real Estate Directory')

// Fetch all users
const { get } = useApi()
const { data: users, pending } = await useAsyncData('users', () => get('/users'))
</script>

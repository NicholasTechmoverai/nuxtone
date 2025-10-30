<template>
  <div class="min-h-screen p-6">
    <NuxtLink to="/user" class="text-gray-500 hover:underline mb-4 inline-block">
      ← Back
    </NuxtLink>

    <div v-if="pending" class="text-center text-gray-600 mt-10">
      Loading user...
    </div>

    <div v-else-if="user" class="max-w-xl mx-auto">
      <UCard class="p-6 text-center">
        <UAvatar :src="user.avatar" :alt="user.name" size="2xl" class="mx-auto mb-4" />
        <h2 class="text-2xl font-semibold text-gray-800">{{ user.name }}</h2>
        <p class="text-gray-600 mb-2">{{ user.email }}</p>
        <UBadge :color="user.role === 'premium' ? 'amber' : 'gray'" class="mb-3">
          {{ user.role }}
        </UBadge>

        <p class="text-gray-700 italic mb-3">“{{ user.bio }}”</p>
        <div class="text-sm text-gray-600 space-y-1">
          <p><strong>📍 Location:</strong> {{ user.location }}</p>
          <p><strong>📞 Phone:</strong> {{ user.phone }}</p>
          <p><strong>Joined:</strong> {{ new Date(user.created_at).toLocaleDateString() }}</p>
        </div>
      </UCard>
    </div>

    <p v-else class="text-center text-gray-600 mt-10">User not found.</p>
  </div>
</template>

<script setup lang="ts">
import { useApi } from '~/composables/useApi'
import { useSeo } from '~/composables/useSeo'

const route = useRoute()
const { get } = useApi()

// Fetch user by ID
const { data: user, pending } = await useAsyncData(`user-${route.params.id}`, () =>
  get(`/users/${route.params.id}`)
)

// Wait for data to be available before setting SEO
watchEffect(() => {
  if (user.value) {
    useSeo(
      `${user.value.name} - ${user.value.role|| ''}`,
      user.value.bio || 'User profile on Real Estate Directory',
      user.value.avatar
    )
  }
})
</script>

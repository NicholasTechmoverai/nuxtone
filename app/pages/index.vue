<template>
  <UContainer class="py-8">
    <h1 class="text-3xl font-bold mb-6">Latest Posts</h1>

    <div v-if="pending" class="text-gray-500">Loading posts...</div>

    <div v-else class="grid gap-4">
      <PostCard v-for="post in posts" :key="post.id" :post="post" />
    </div>
  </UContainer>
</template>

<script setup lang="ts">
import PostCard from '~/components/PostCard.vue'
import { useApi } from '~/composables/useApi'
import { useSeo } from '~/composables/useSeo'

useSeo('Nuxt + FastAPI Demo', 'A simple Nuxt + FastAPI integration demo.')

const { get } = useApi()
const { data: posts, pending } = await useAsyncData('posts', () => get('/posts'))
</script>

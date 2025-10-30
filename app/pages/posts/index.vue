<template>
  <UContainer class="py-12">
    <h1 class="text-4xl font-bold mb-8 text-center">📰 Latest Posts</h1>

    <div v-if="pending" class="text-gray-500 text-center">Loading posts...</div>

    <div v-else class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
      <UCard
        v-for="post in posts"
        :key="post.id"
        class="hover:shadow-lg transition-all duration-300 cursor-pointer"
        @click="navigateTo(`/posts/${post.id}`)"
      >
        <img
          :src="post.image"
          alt="Post image"
          class="w-full h-48 object-cover rounded-t-lg"
        />
        <div class="p-4 space-y-2">
          <h2 class="text-xl font-semibold line-clamp-2">{{ post.title }}</h2>
          <p class="text-gray-600 text-sm line-clamp-3">{{ post.content }}</p>
          <div class="flex justify-between items-center text-sm text-gray-500 pt-2">
            <span>❤️ {{ post.likes }}</span>
            <span>💬 {{ post.comments }}</span>
          </div>
        </div>
      </UCard>
    </div>
  </UContainer>
</template>

<script setup lang="ts">
import { useApi } from '~/composables/useApi'
import { useSeo } from '~/composables/useSeo'

useSeo('Latest Posts', 'Explore inspiring real estate stories and market insights.')

const { get } = useApi()
const { data: posts, pending } = await useAsyncData('posts', () => get('/posts'))
</script>

<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">Posts</h1>
    <div v-if="pending">Loading posts...</div>
    <div v-else>
      <div class="space-y-4">
        <div v-for="post in posts" :key="post.id" class="border p-4 rounded">
          <h2 class="text-lg font-semibold">
            <NuxtLink :to="`/posts/${post.id}`">{{ post.title }}</NuxtLink>
          </h2>
          <p class="text-gray-600">{{ post.content.slice(0, 100) }}...</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Post { id: string; title: string; content: string }
const { data: posts, pending } = await useApi<Post[]>('/posts')
useHead({ title: 'Posts - Nuxt + FastAPI Demo' })
</script>

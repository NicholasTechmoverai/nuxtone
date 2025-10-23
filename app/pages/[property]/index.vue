<template>
  <UContainer class="p-6">
    <h1 class="text-2xl font-bold mb-4">Nuxt + FastAPI Test</h1>
    <UButton @click="fetchPosts" label="Fetch Posts" color="primary" class="mb-4" />
    <div v-if="posts.length" class="space-y-2">
      <div v-for="post in posts" :key="post.id" class="p-4 border rounded-lg">
        <h2 class="font-semibold text-lg">{{ post.title }}</h2>
        <p>{{ post.content }}</p>
      </div>
    </div>
  </UContainer>
</template>

<script setup>
const posts = ref([])

async function fetchPosts() {
  const res = await fetch('http://127.0.0.1:8000/posts')
  const data = await res.json()
  posts.value = data.posts
}
</script>

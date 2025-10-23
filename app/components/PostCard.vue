<template>
  <NuxtLink
    :to="`/posts/${post.id}`"
    class="block border rounded-xl p-4 hover:shadow-md transition"
  >
    <h2 class="text-xl font-semibold">{{ post.title }}</h2>
    <p class="text-gray-600 mt-2 line-clamp-2">{{ post.content }}</p>
  </NuxtLink>
</template>

<script setup lang="ts">
defineProps({
  post: { type: Object, required: true },
})
</script>

<template>
  <UContainer class="py-10">
    <div v-if="pending" class="text-gray-500">Loading post...</div>
    <article v-else>
      <h1 class="text-3xl font-bold mb-2">{{ post.title }}</h1>
      <p class="text-gray-600 mb-6">By User {{ post.author }}</p>
      <p>{{ post.content }}</p>
    </article>
  </UContainer>
</template>

<script setup lang="ts">
import { useApi } from '~/composables/useApi'
import { useSeo } from '~/composables/useSeo'

const route = useRoute()
const { get } = useApi()
const { data: post, pending } = await useAsyncData(`post-${route.params.id}`, () =>
  get(`/posts/${route.params.id}`)
)

useSeo(post.value?.title || 'Post', post.value?.content.slice(0, 100))
</script>

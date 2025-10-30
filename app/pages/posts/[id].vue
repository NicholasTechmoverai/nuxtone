<template>
  <UContainer class="py-10 max-w-3xl mx-auto">
    <div v-if="pending" class="text-gray-500 text-center">Loading post...</div>

    <article v-else class="space-y-6">
      <img
        :src="post?.image"
        alt="Post banner"
        class="w-full h-64 object-cover rounded-xl shadow-md"
      />

      <div class="space-y-3">
        <h1 class="text-4xl font-bold">{{ post.title }}</h1>
        <p class="text-gray-500 text-sm">
          📅 {{ new Date(post.created_at).toLocaleDateString() }} |
          ✍️ Author ID: {{ post.author }}
        </p>
      </div>

      <p class="leading-relaxed text-gray-700">{{ post.content }}</p>

      <div class="flex justify-between items-center text-gray-500 pt-4 border-t">
        <span>❤️ {{ post.likes }} Likes</span>
        <span>💬 {{ post.comments }} Comments</span>
      </div>
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

watchEffect(() => {
  if (post.value) {
    useSeo(
      post.value.title || 'Post',
      post.value.content.slice(0, 150),
      post.value.image
    )
  }
})
</script>

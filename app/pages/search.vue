<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">Search Posts</h1>
    <input
      v-model="query"
      type="text"
      placeholder="Search posts..."
      class="border p-2 w-full rounded"
      @input="onSearch"
    />
    <div v-if="pending" class="mt-4">Searching...</div>
    <div v-else-if="results.length" class="mt-4 space-y-4">
      <div v-for="r in results" :key="r.id" class="border p-3 rounded">
        <h2 class="text-lg font-semibold">{{ r.title }}</h2>
        <p>{{ r.content }}</p>
      </div>
    </div>
    <p v-else class="mt-4 text-gray-500">No results</p>
  </div>
</template>

<script setup lang="ts">
const query = ref('')
const results = ref([])
const pending = ref(false)

const onSearch = async () => {
  if (!query.value.trim()) {
    results.value = []
    return
  }
  pending.value = true
  const { data } = await useFetch(`/api/search?q=${query.value}`)
  results.value = data.value.results
  pending.value = false
}

useHead({ title: 'Search - Nuxt + FastAPI Demo' })
</script>

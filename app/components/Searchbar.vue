<script setup lang="ts">
import { ref } from 'vue'

const search = ref('')

const emit = defineEmits<{
  (e: 'handleSearch', value: string): void
}>()

function onSearch() {
  const query = search.value.trim()
  if (query) emit('handleSearch', query)
}
</script>

<template>
  <div class="flex items-center gap-2  w-fit border-1 border-gray-5/20 m-2 p-2 rounded-sm">
    <UInput v-model="search" highlight size="xl" placeholder="Search for properties, e.g. '2 bedroom condo in Madison'"
      @keyup.enter="onSearch" />
    <UButton size="xl" :disabled="!search.trim()" @click="onSearch">
      Search
    </UButton>
  </div>
</template>

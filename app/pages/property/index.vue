<template>
<div class="p-6">
<h1 class="text-3xl font-bold mb-6">All Properties</h1>
<SearchBar @handleSearch="handleSearch" />


<div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
<UCard v-for="property in properties" :key="property.id">
<img :src="property.image" :alt="property.title" class="rounded-lg mb-3" />
<h3 class="font-semibold text-lg">{{ property.title }}</h3>
<p class="text-gray-600 mb-2">{{ property.location }}</p>
<UBadge>{{ property.property_type }}</UBadge>
<p class="text-sm mt-2">💰 ${{ property.price.toLocaleString() }}</p>


<template #footer>
<NuxtLink :to="`/property/${property.property_type.toLowerCase()}/${property.id}`" class="text-primary hover:underline">
View Details →
</NuxtLink>
</template>
</UCard>
</div>
</div>
</template>


<script setup lang="ts">
import { useApi } from '~/composables/useApi'
import SearchBar from '~/components/Searchbar.vue'
const { get } = useApi()

import { useSeo } from '~/composables/useSeo'

useSeo(
      `properties`,
     ' trending proerties',
    )
const { data: properties } = await useAsyncData('properties', () => get('/properties'))



async function handleSearch(query: string) {
  console.log('User searched:', query)
  navigateTo(`/properties/${query}`)
}
</script>
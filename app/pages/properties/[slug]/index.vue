<script setup lang="ts">
import { useRoute } from '#imports'
import { useSeoMeta } from '#imports'

const route = useRoute()
const slug = computed(() => route.params.slug)

const runtimeConfig = useRuntimeConfig()

const { data, pending, error } = await useFetch(
  () => `${runtimeConfig.public.apiBase}/search-properties/v2/nlp-search`,
  {
    query: { query: slug.value },
    headers: { Accept: 'application/json' }
  }
)

console.log(data.value)

const results = computed(() => data.value?.properties ?? [])
const seo = computed(() => data.value?.seo ?? {})
const filters = computed(() => data.value?.filters ?? {})
useSeoMeta({
  title: () => seo.value?.title || `Search "${slug.value}"`,
  description: () => seo.value?.description || `Properties for ${slug.value}`,
  ogTitle: () => seo.value?.title,
  ogDescription: () => seo.value?.description,
  ogImage: () => seo.value?.image
})
</script>

<template>
  <div class="p-6 max-w-7xl mx-auto">

    <h1 class="text-2xl font-bold mb-6">
      Property search results for "<span class="text-blue-600">{{ slug }}</span>"
    </h1>


    <div>
      <p class="font-semibold mb-2">Filters</p>

      <div v-for="(value, key) in filters" :key="key"
        class="flex items-center gap-2 border border-gray-300 rounded px-2 py-1 text-sm w-fit mb-2">
        <span class="font-medium capitalize">{{ key }}:</span>

        <!-- If value is array, join it nicely -->
        <span>
          {{ Array.isArray(value) ? value.join(', ') : value }}
        </span>
      </div>
    </div>

    <div v-if="pending" class="text-center py-16 text-gray-500">
      Loading properties...
    </div>

    <div v-else-if="error" class="text-red-600 font-medium text-center py-10">
      Failed to load results. Please try again.
    </div>

    <div v-else-if="!results.length" class="text-gray-600 py-16 text-center">
      No properties found for "<strong>{{ slug }}</strong>"
    </div>

    <!-- Results Grid -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
      <article v-for="property in results" :key="property.id"
        class="bg-white border border-gray-200 rounded-xl overflow-hidden hover:shadow-lg transition-all duration-300 hover:scale-[1.02]">
        <img :src="property.image" :alt="property.title" class="w-full h-48 object-cover" loading="lazy" />

        <div class="p-4">
          <h2 class="text-lg font-semibold text-gray-900 mb-1 line-clamp-1">
            {{ property.title }}
          </h2>

          <p class="text-gray-600 text-sm mb-2 flex items-center">
            <span class="mr-1">📍</span>
            <span class="line-clamp-1">{{ property.location }}</span>
          </p>

          <div class="flex items-center gap-4 text-sm text-gray-500 mb-3">
            <span>🛏️ {{ property.bedrooms }} bed{{ property.bedrooms !== 1 ? 's' : '' }}</span>
            <span>🛁 {{ property.bathrooms }} bath{{ property.bathrooms !== 1 ? 's' : '' }}</span>
            <span v-if="property.square_feet">📐 {{ property.square_feet.toLocaleString() }} sqft</span>
          </div>

          <p class="font-bold text-lg text-blue-600 mb-2">
            ${{ property.price.toLocaleString() }}
          </p>

          <p class="text-gray-700 text-sm line-clamp-2">
            {{ property.description }}
          </p>

          <div class="mt-3 pt-3 border-t border-gray-100">
            <span class="inline-block bg-gray-100 text-gray-700 px-2 py-1 rounded text-xs font-medium">
              {{ property.property_type }}
            </span>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

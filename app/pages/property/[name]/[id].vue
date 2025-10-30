<template>
<div class="p-6 max-w-3xl mx-auto">
<NuxtLink :to="`/property/${route.params.name}`" class="text-gray-500 hover:underline mb-4 inline-block">
← Back to {{ route.params.name }}
</NuxtLink>


<div v-if="property" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
<img :src="property.image" :alt="property.title" class="rounded-lg mb-6 w-full" />
<h2 class="text-3xl font-bold mb-2">{{ property.title }}</h2>
<p class="text-gray-600 mb-2">📍 {{ property.location }}</p>
<UBadge :to="property.property_type" class="mb-3">{{ property.property_type }}</UBadge>
<p class="text-lg mb-4">💰 ${{ property.price.toLocaleString() }}</p>


<div class="text-gray-700 space-y-2">
<p><strong>Bedrooms:</strong> {{ property.bedrooms }}</p>
<p><strong>Bathrooms:</strong> {{ property.bathrooms }}</p>
<p><strong>Area:</strong> {{ property.square_feet }} sq ft</p>
<p><strong>Year Built:</strong> {{ property.year_built }}</p>
<p><strong>Description:</strong> {{ property.description }}</p>
</div>
<NuxtLink :to="`/property/${property.property_type }`" class="text-primary hover:underline">
view similar →
</NuxtLink>
</div>




<p v-else class="text-center mt-10 text-gray-600">Loading property...</p>
</div>
</template>


<script setup lang="ts">
import { useApi } from '~/composables/useApi'
const route = useRoute()
const { get } = useApi()
import { useSeo } from '~/composables/useSeo'


const { data: property } = await useAsyncData(`property-${route.params.id}`, () =>
get(`/properties/${route.params.id}`)
)

watchEffect(() => {
  if (property.value) {
    useSeo(
      `${property.value.title} - ${property.value.location || ''}`,
      property.value.description || 'property',
      property.value.image
    )
  }
})

</script>
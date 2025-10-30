<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import { useApi } from '~/composables/useApi'
import { useSeo } from '~/composables/useSeo'

const route = useRoute()
const router = useRouter()
const { name } = route.params
const { get } = useApi()

const { data: properties } = await useAsyncData(`properties-${name}`, () =>
  get(`/properties/type/${name}`)
)

useSeo(
  `Best ${name}s for Sale and Rent`,
  `Explore the best ${name}s with detailed descriptions, images, and pricing.`
)

function openProperty(p) {
  router.push(`/property/${name}/${p.id}`)
}
</script>

<template>
  <section>
    <h1>{{ name }} Listings</h1>
    <div v-if="properties?.length">
      <div v-for="p in properties" :key="p.id" @click="openProperty(p)" class="cursor-pointer">
        <img :src="p.image" :alt="p.title" class="rounded-lg" />
        <h2>{{ p.title }}</h2>
        <p>{{ p.location }} - {{ p.price.toLocaleString() }} USD</p>
      </div>
    </div>
    <p v-else>No properties found.</p>
  </section>
</template>

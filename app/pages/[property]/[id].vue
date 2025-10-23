<template>
  <div class="p-8">
    <h1 class="text-xl font-semibold capitalize">
      {{ property }} ID: {{ id }}
    </h1>
    <NuxtLink :to="`/${property}`" class="text-blue-500 underline">
      Back to {{ property }} list
    </NuxtLink>
  </div>
</template>

<script setup>
const route = useRoute()
const { property, id } = route.params
</script>

<template>
  <div class="text-center py-12">
    <h1 class="text-3xl font-bold mb-2 text-red-600">404 - Page Not Found</h1>
    <p>The page you’re looking for doesn’t exist.</p>
    <NuxtLink to="/" class="btn mt-6">Go Home</NuxtLink>
  </div>
</template>

<script setup>
useHead({ title: '404 - Page Not Found' })
</script>

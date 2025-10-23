<template>
  <UContainer class="min-h-screen flex flex-col items-center justify-center text-center py-20">
    <h1 class="text-5xl font-bold text-red-500 mb-6">{{ error.statusCode }}</h1>
    <p class="text-lg text-gray-600 dark:text-gray-300 mb-8">
      {{ message }}
    </p>
    <UButton to="/" color="primary" label="Go back home" />
  </UContainer>
</template>

<script setup>
const props = defineProps({
  error: Object
})

// Customize the message
const message = computed(() => {
  if (props.error.statusCode === 404)
    return "Sorry, the page you’re looking for doesn’t exist."
  return props.error.message || "Something went wrong."
})

// Optionally clear error when navigating away
const handleError = useError()
onMounted(() => {
  handleError.value = null
})
</script>

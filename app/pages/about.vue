<template>
  <UCard>
    <template #header>
      <h3 class="text-lg font-semibold">Error Testing</h3>
    </template>

    <UButton @click="testError" color="red">
      Test Error Response
    </UButton>

    <UButton @click="testSlow" class="ml-2" color="orange">
      Test Slow Request
    </UButton>
  </UCard>
</template>

<script setup>
const testError = async () => {
  try {
    const { data, error } = await useFetch('http://localhost:8000/simulate-error')
    if (error.value) {
      console.error('Error response:', error.value)
      // Handle error in UI
    }
  } catch (error) {
    console.error('Request failed:', error)
  }
}

const testSlow = async () => {
  const { data } = await useFetch('http://localhost:8000/slow-data?delay=3')
  console.log('Slow response:', data.value)
}
</script>
<template>
  <div>
    <Navbar />
    <main class="p-6">
      <slot />
    </main>
    <Footer />
  </div>
</template>

<script setup>
import Navbar from '~/components/Navbar.vue'
import Footer from '~/components/Footer.vue'
</script>

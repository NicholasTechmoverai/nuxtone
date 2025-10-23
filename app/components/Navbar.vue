<template>
  <nav class="flex justify-between items-center px-8 py-4 bg-gray-800 text-white">
    <div class="text-xl font-bold">NuxtDemo</div>
    <div class="space-x-4">
      <NuxtLink to="/" class="hover:text-blue-400">Home</NuxtLink>
      <NuxtLink to="/users" class="hover:text-blue-400">Users</NuxtLink>
      <NuxtLink to="/posts" class="hover:text-blue-400">Posts</NuxtLink>
      <NuxtLink to="/search" class="hover:text-blue-400">Search</NuxtLink>
    </div>
  </nav>
</template>

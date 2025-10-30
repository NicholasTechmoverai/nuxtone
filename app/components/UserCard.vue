<template>
  <UCard 
    class="group cursor-pointer hover:shadow-xl transition-all duration-300 border-l-4"
    :class="roleBorderClass"
    @click="navigateToUser"
  >
    <!-- Header with avatar and actions -->
    <div class="flex items-start justify-between mb-4">
      <div class="flex items-center gap-3">
        <UAvatar
          :alt="user.name"
          size="lg"
          :ui="{ rounded: 'rounded-xl' }"
          class="ring-2 ring-white shadow-lg"
        />
        <div>
          <h3 class="font-semibold text-gray-900 group-hover:text-primary transition-colors">
            {{ user.name }}
          </h3>
          <UBadge 
            :color="roleBadgeColor" 
            variant="subtle" 
            size="sm"
            class="mt-1"
          >
            {{ user.role }}
          </UBadge>
        </div>
      </div>
      <UButton
        icon="i-heroicons-ellipsis-vertical"
        color="gray"
        variant="ghost"
        size="sm"
        @click.stop="openMenu"
      />
    </div>

    <!-- User info -->
    <div class="space-y-3 mb-4">
      <div class="flex items-center gap-2 text-sm text-gray-600">
        <UIcon name="i-heroicons-envelope" class="w-4 h-4 flex-shrink-0" />
        <span class="truncate">{{ user.email }}</span>
      </div>
      <div class="flex items-center gap-2 text-sm text-gray-600">
        <UIcon name="i-heroicons-calendar" class="w-4 h-4 flex-shrink-0" />
        <span>{{ formatDate(user.created_at) }}</span>
      </div>
    </div>

    <!-- Stats -->
    <div class="grid grid-cols-2 gap-3 mb-4">
      <div class="text-center p-2 bg-blue-50 rounded-lg">
        <UIcon name="i-heroicons-document-text" class="w-5 h-5 text-blue-600 mx-auto mb-1" />
        <p class="text-sm font-semibold text-gray-900">{{ user.posts?.length || 0 }}</p>
        <p class="text-xs text-gray-600">Posts</p>
      </div>
      <div class="text-center p-2 bg-green-50 rounded-lg">
        <UIcon name="i-heroicons-home" class="w-5 h-5 text-green-600 mx-auto mb-1" />
        <p class="text-sm font-semibold text-gray-900">{{ user.properties?.length || 0 }}</p>
        <p class="text-xs text-gray-600">Properties</p>
      </div>
    </div>

    <!-- Action buttons -->
    <div class="flex gap-2 pt-4 border-t border-gray-200">
      <UButton
        color="primary"
        variant="outline"
        size="sm"
        class="flex-1"
        @click.stop="navigateToUser"
      >
        View Profile
      </UButton>
      <UButton
        icon="i-heroicons-chat-bubble-left-right"
        color="gray"
        variant="outline"
        size="sm"
        @click.stop="sendMessage"
      />
    </div>
  </UCard>

  <!-- Dropdown Menu -->
  <UDropdown
    v-model="isMenuOpen"
    :items="menuItems"
    :popper="{ placement: 'bottom-end' }"
  />
</template>

<script setup lang="ts">
interface User {
  id: string
  name: string
  email: string
  role: string
  created_at: string
  posts?: any[]
  properties?: any[]
}

const props = defineProps<{ user: User }>()
const toast = useToast()

// State
const isMenuOpen = ref(false)

// Computed
const roleBorderClass = computed(() => {
  const classes = {
    admin: 'border-l-red-500',
    premium: 'border-l-purple-500',
    user: 'border-l-blue-500'
  }
  return classes[props.user.role as keyof typeof classes] || 'border-l-gray-500'
})

const roleBadgeColor = computed(() => {
  const colors = {
    admin: 'red',
    premium: 'purple',
    user: 'blue'
  }
  return colors[props.user.role as keyof typeof colors] || 'gray'
})

const menuItems = computed(() => [
  [{
    label: 'View Profile',
    icon: 'i-heroicons-user',
    click: navigateToUser
  }, {
    label: 'Send Message',
    icon: 'i-heroicons-envelope',
    click: sendMessage
  }],
  [{
    label: 'View Posts',
    icon: 'i-heroicons-document-text',
    click: viewPosts
  }, {
    label: 'View Properties',
    icon: 'i-heroicons-home',
    click: viewProperties
  }]
])

// Methods
const navigateToUser = () => {
  navigateTo(`/users/${props.user.id}`)
}

const sendMessage = () => {
  toast.add({
    title: 'Message sent!',
    description: `Message initiated with ${props.user.name}`,
    icon: 'i-heroicons-check',
    color: 'green'
  })
}

const viewPosts = () => {
  navigateTo(`/users/${props.user.id}?tab=posts`)
}

const viewProperties = () => {
  navigateTo(`/users/${props.user.id}?tab=properties`)
}

const openMenu = () => {
  isMenuOpen.value = true
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}
</script>

<style scoped>
.group:hover .group-hover\:text-primary {
  color: rgb(59 130 246);
}
</style>
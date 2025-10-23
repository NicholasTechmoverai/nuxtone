// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',

  devtools: { enabled: false },

  modules: [
    '@nuxt/ui',
    '@unocss/nuxt',
    '@nuxtjs/color-mode'
  ],
  css: ['~/assets/css/main.css'],
  unocss: {
    nuxtLayers: true,
    attributify: true,
    icons: true,
    typography: true,
    preflight: true
  },

  // ✅ Configure color modes (light/dark)
  colorMode: {
    preference: 'system',
    fallback: 'light',
    classSuffix: ''
  },

  app: {
    head: {
      title: 'NuxtOne | Modern SSR UI',
      meta: [
        { name: 'description', content: 'A Nuxt 4 project powered by Nuxt UI and UnoCSS' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' }
      ],
      link: [
        { rel: 'icon', type: 'image/png', href: '/favicon.png' }
      ]
    }
  },
  runtimeConfig: {
    public: {
      apiBase: 'http://127.0.0.1:8000', // FastAPI URL
    },
  },
  // SSR & Rendering
  ssr: true,
  nitro: {
    preset: 'node-server'
  }
})

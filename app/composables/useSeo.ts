export const useSeo = (
  title?: string,
  description?: string,
  image?: string
) => {
  const runtimeConfig = useRuntimeConfig()
  const route = useRoute()

  // 🌍 Base site URL for canonical and OG
  const baseUrl =
    runtimeConfig.public.siteUrl || 'https://injustify.tera-in.top'

  // ✅ Default fallbacks
  const defaultTitle = 'Injustify Real Estate'
  const defaultDescription =
    'Discover, explore, and list amazing real estate properties around the world. Built with Nuxt + FastAPI.'
  const defaultImage = `${baseUrl}/default-preview.png`
  const favicon = '/favicon.png'

  // 🧩 Computed SEO fields
  const seoTitle = title ? `${title} | Nuxt One` : defaultTitle
  const seoDescription = description || defaultDescription
  const seoImage = image || defaultImage
  const canonical = `${baseUrl}${route.fullPath}`

  useHead({
    title: seoTitle,
    meta: [
      // 🔹 Basic meta
      { name: 'description', content: seoDescription },
      { name: 'author', content: 'Injustify' },

      // 🔹 Open Graph
      { property: 'og:title', content: seoTitle },
      { property: 'og:description', content: seoDescription },
      { property: 'og:image', content: seoImage },
      { property: 'og:url', content: canonical },
      { property: 'og:type', content: 'website' },
      { property: 'og:site_name', content: 'Injustify Real Estate' },

      // 🔹 Twitter
      { name: 'twitter:card', content: 'summary_large_image' },
      { name: 'twitter:title', content: seoTitle },
      { name: 'twitter:description', content: seoDescription },
      { name: 'twitter:image', content: seoImage },
      { name: 'twitter:creator', content: '@Injustify' },

      // 🔹 Robots & SEO helpers
      { name: 'robots', content: 'index, follow' },
      { name: 'theme-color', content: '#ffffff' },
    ],
    link: [
      { rel: 'icon', type: 'image/png', href: favicon },
      { rel: 'canonical', href: canonical },
      { rel: 'apple-touch-icon', href: favicon },
    ],
  })
}

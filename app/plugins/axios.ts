// app/plugins/axios.ts
import axios from 'axios'

export default defineNuxtPlugin((nuxtApp) => {
  const api = axios.create({
    baseURL: 'https://api.example.com',
    timeout: 8000
  })

  // Example: interceptors
  api.interceptors.request.use((config) => {
    const token = useCookie('token').value
    if (token) config.headers.Authorization = `Bearer ${token}`
    return config
  })

  // Inject globally
  nuxtApp.provide('api', api)
})

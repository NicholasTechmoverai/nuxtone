export const useApi = () => {
  const config = useRuntimeConfig()

  async function get(endpoint: string) {
    return await $fetch(`${config.public.apiBase}${endpoint}`)
  }

  async function post(endpoint: string, body: any) {
    return await $fetch(`${config.public.apiBase}${endpoint}`, {
      method: 'POST',
      body,
    })
  }

  return { get, post }
}

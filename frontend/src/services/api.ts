import axios from 'axios'

const baseURL = import.meta.env.VITE_API_BASE_URL || ''

const api = axios.create({
  baseURL,
  headers: { 'Content-Type': 'application/json' },
})

api.interceptors.request.use((config) => {
  const raw = localStorage.getItem('user')
  if (raw) {
    try {
      const user = JSON.parse(raw) as { token?: string } | null
      if (user?.token) {
        config.headers.Authorization = `Bearer ${user.token}`
      }
    } catch {
      // ignore invalid storage
    }
  }
  return config
})

export default api

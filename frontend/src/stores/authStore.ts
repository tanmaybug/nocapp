import { defineStore } from 'pinia'
import type { Status } from '@/types/common'
import { submitLogin } from '@/apis'

type LoginForm = { username: string; password: string }

function defaultForm(): LoginForm {
  return {
    username: '',
    password: '',
  }
}

interface AuthState {
  user: { token: string } | null
  status: Status
  error: string | null
  form: LoginForm
}

export const useAuthStore = defineStore('auth', {
  state: (): AuthState => ({
    user: localStorage.getItem('token') ? { token: localStorage.getItem('token')! } : null,
    status: 'initialized',
    error: null,
    form: defaultForm(),
  }),
  getters: {
    isAuthenticated: (state) => !!state.user?.token,
  },
  actions: {
    resetForm() {
      this.form = defaultForm()
    },
    async login(): Promise<void> {
      this.status = 'processing'
      this.error = null
      try {
        const response = await submitLogin(this.form)
        this.status = 'processed'
        this.user = { token: response.data.token }
        localStorage.setItem('token', response.data.token)
        this.resetForm()
      } catch (err: any) {
        this.status = 'failed'
        this.error = err?.response?.data?.message || err?.message || 'Login failed'
        throw err
      }
    },
    logout() {
      localStorage.removeItem('token')
      this.user = null
    }
  },
})

export default useAuthStore

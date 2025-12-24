import { defineStore } from 'pinia'
import type { Status } from '@/types/common'
import { submitLogin } from '@/modules/auth/services/auth.service'

export const ROLE = {
  DEPARTMENT: 'DEPARTMENT',
  INSTITUTION: 'INSTITUTION',
} as const

export type Role = typeof ROLE[keyof typeof ROLE]
type LoginForm = {
  username: string
  password: string
}
export type User  = {
  token: string
  role: Role
  name: string
}
export type AuthState = {
  user: User | null
  status: Status
  error: string | null
  form: LoginForm
}

function defaultForm(): LoginForm {
  return {
    username: '',
    password: '',
  }
}

export const useAuthStore = defineStore('auth', {
  state: (): AuthState => ({
    user: localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')!): null,
    status: 'initialized',
    error: null,
    form: defaultForm(),
  }),
  getters: {
    isAuthenticated: (state) => !!state.user?.token,
    role: (state) => state.user?.role || null,
  },
  actions: {
    resetForm() {
      this.form = defaultForm()
      this.error = null
      this.status = 'initialized'
    },
    async login(): Promise<void> {
      this.status = 'processing'
      this.error = null
      try {
        const response = await submitLogin(this.form)
        this.status = 'processed'
        localStorage.setItem('user', JSON.stringify(response.data))
        this.user = { ...response.data }
        this.resetForm()
      } catch (err: any) {
        this.status = 'failed'
        this.error = err?.response?.data?.message || err?.message || 'Login failed'
      }
    },
    logout() {
      localStorage.removeItem('user')
      this.user = null
    }
  },
})

export default useAuthStore

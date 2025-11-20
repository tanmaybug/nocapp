import { defineStore } from 'pinia'
import type { Status } from '@/types/common'
import { submitLogin } from '@/apis'

function defaultForm() {
  return {
    username: '',
    password: '',
  }
}

export const useAuthStore = defineStore('auth', {
  state: (): { status: Status; error: string | null; form: { username: string; password: string }; user: { token: string } | null } => ({
    user: null,
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
    async login() {
      this.status = 'processing'
      this.error = null
      try {
        const response = await submitLogin(this.form)
        this.status = 'processed'
        this.user = { token: response.data.token }
      } catch (err: any) {
        this.status = 'failed'
        this.error = err?.response?.data?.message || err?.message || 'Login failed'
        alert(this.error)
        throw err
      }
    },
  },
})

export default useAuthStore

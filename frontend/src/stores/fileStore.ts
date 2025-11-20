import { defineStore } from 'pinia'
import api from '@/apis'
import type { Status } from '@/types/common'

export const useFileStore = defineStore('file', {
  state: (): {
    status: Status
    error: string | null
    lastResponse: any | null
    progress: number
  } => ({
    status: 'initialized',
    error: null,
    lastResponse: null,
    progress: 0,
  }),

  actions: {
    async uploadFile(formData: FormData, onProgress?: (p: number) => void) {
      this.status = 'processing'
      this.error = null
      this.progress = 0

      try {
        const resp = await api.post('/files/upload', formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
          onUploadProgress: (evt: any) => {
            const loaded = evt?.loaded ?? 0
            const total = evt?.total ?? 0
            if (!total) return
            const percent = Math.round((loaded * 100) / total)
            this.progress = percent
            if (onProgress) onProgress(percent)
          },
        })

        this.lastResponse = resp.data
        this.status = 'processed'
        this.progress = 100
        return resp.data
      } catch (err: any) {
        this.status = 'failed'
        this.error = err?.response?.data?.message || err?.message || 'Upload failed'
        throw err
      }
    },

    reset() {
      this.status = 'initialized'
      this.error = null
      this.lastResponse = null
      this.progress = 0
    },
  },
})

export default useFileStore

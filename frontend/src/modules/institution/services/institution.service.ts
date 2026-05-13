import api from '@/services/api'
import type { NOCFormType } from '@/modules/institution/stores'

const RESOURCE_BASE = '/institution'

export const submitNocForm = async (nocFormURL: NOCFormType, payload: any) => {
  const resp = await api.post(`${RESOURCE_BASE}/${nocFormURL}`, payload)
  return resp.data
}

export const uploadFile = async (file: File) => {
  const formData = new FormData()
  formData.append('file', file)
  const resp = await api.post(`${RESOURCE_BASE}/fileUpload`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  })
  return resp.data?.data ?? resp.data
}

export const saveFile = async (payload: { fileId: number; documentType: string; documentTypeId: number }) => {
  const resp = await api.post(`${RESOURCE_BASE}/saveFile`, payload)
  return resp.data?.data ?? resp.data
}

export const getDashboardData = async () => {
  const resp = await api.get(`${RESOURCE_BASE}/Dashboard`)
  return resp.data
}

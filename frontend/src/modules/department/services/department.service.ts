import api from '@/services/api'
import type { NOCApplicationType } from '../stores/departmentStore'

const RESOURCE_BASE = '/department'


export const getDashboardData = async () => {
  const resp = await api.get(`${RESOURCE_BASE}/Dashboard`)
  return resp.data
}

export const getNOCApplicationsByStatus = async (nocApplicationType: NOCApplicationType) => {
  const resp = await api.get(`${RESOURCE_BASE}/noc-applications/${nocApplicationType}`)
  return resp.data
}
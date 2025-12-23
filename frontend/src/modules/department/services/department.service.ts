import api from '@/services/api'

const RESOURCE_BASE = '/department'


export const getDashboardData = async () => {
  const resp = await api.get(`${RESOURCE_BASE}/Dashboard`)
  return resp.data
}

export const getPendingApplications = async () => {
  const resp = await api.get(`${RESOURCE_BASE}/PendingNOCApplications`)
  return resp.data
}

export const getInprocessApplications = async () => {
  const resp = await api.get(`${RESOURCE_BASE}/InProcessNOCApplications`)
  return resp.data
}

export const getCompletedApplications = async () => {
  const resp = await api.get(`${RESOURCE_BASE}/CompletedNOCApplications`)
  return resp.data
}

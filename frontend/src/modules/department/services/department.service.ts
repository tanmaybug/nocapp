import api from '@/services/api'

const RESOURCE_BASE = '/department'

export const getDashboardData = async () => {
  const resp = await api.get(`${RESOURCE_BASE}/Dashboard`)
  return resp.data
}

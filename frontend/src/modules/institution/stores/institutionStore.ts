import { defineStore } from 'pinia'
import type { Status } from '@/types/common'
import { getDashboardData } from '@/modules/institution/services/institution.service'

export const ACTIVITY_STATUS = {
  PENDING: 'PENDING',
  COMPLETED: 'COMPLETED',
} as const
export type ActivityStatus = typeof ACTIVITY_STATUS[keyof typeof ACTIVITY_STATUS]
export type Activity = {
  sno: number
  activity: string
  date: string
  status: ActivityStatus
}
export type InstitutionState = {
  dashboardData: {
    currentStatus: string | null
    lastUpdatedDate: String | null
    inspectionDate: string | null
    isNOCCompleted: boolean
    activities: Activity[]
  }
  status: Status
  error: string | null
}

export const useInstitutionStore = defineStore('institution', {
  state: (): InstitutionState => ({
    dashboardData: {
      currentStatus: null,
      lastUpdatedDate: null,
      inspectionDate: null,
      isNOCCompleted: false,
      activities: []
    },
    status: 'initialized',
    error: null,
  }),
  actions: {
    async getDashboardData(): Promise<void> {
      this.status = 'processing'
      this.error = null
      try {
        const response = await getDashboardData()
        this.dashboardData = { ...response.data }
      } catch (err: any) {
        this.status = 'failed'
        this.error = err?.response?.data?.message || err?.message || 'Unable to fetch dashboard data'
      }
    },
  },
})

export default useInstitutionStore

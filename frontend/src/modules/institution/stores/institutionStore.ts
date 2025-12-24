import { defineStore } from 'pinia'
import type { Status } from '@/types/common'
import { getDashboardData } from '@/modules/institution/services/institution.service'

export const ACTIVITY_STATUS = {
  PENDING: 'Pending',
  COMPLETED: 'Completed',
} as const
export type ActivityStatus = typeof ACTIVITY_STATUS[keyof typeof ACTIVITY_STATUS]
export type Activity = {
  sno: number
  activity: string
  date: string
  status: ActivityStatus
}
export interface InstitutionState {
  dashboardData: {
    currentStatus: string | null
    lastUpdatedDate: String | null
    isNOCCompleted: boolean
    activities: Activity[]
  }
  status: Status
  error: string | null
}

export const useInstitutionStore = defineStore('institution', {
  state: (): InstitutionState => ({
    dashboardData: {
      currentStatus: "Submitted", // TODO: Set to "UNKNOWN" as default
      lastUpdatedDate: "2025-12-18", // TODO: Set to "UNKNOWN" as default
      isNOCCompleted: false,
      activities: [
        {
          sno: 1,
          activity: 'Form 1',
          date: '2024-06-01',
          status: ACTIVITY_STATUS.COMPLETED
        },
        {
          sno: 2,
          activity: 'Form 2',
          date: '2024-06-01',
          status: ACTIVITY_STATUS.PENDING
        },
      ]
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

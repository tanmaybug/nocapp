import { defineStore } from 'pinia'
import type { Status } from '@/types/common'
import { getDashboardData } from '@/modules/institution/services/institution.service'

export const FORM_STATUS = {
  SUBMITTED: 'Submitted',
  IN_PROCESS: 'In Process',
  NOC_COMPLETED: 'NOC Completed',
} as const
export type FormStatus = typeof FORM_STATUS[keyof typeof FORM_STATUS]

export const TRACK_DATA_STATUS = {
  PENDING: 'Pending',
  DONE: 'Done',
}
export type TrackDataStatus = typeof TRACK_DATA_STATUS[keyof typeof TRACK_DATA_STATUS]
export type TrackData = {
  object: string
  date: string
  status: TrackDataStatus
}
export interface InstitutionState {
  dashboardData: {
    currentStatus: FormStatus | null
    lastUpdatedDate: String | null
    isNOCCompleted: boolean
    trackData: TrackData[]
  }
  status: Status
  error: string | null
}

export const useInstitutionStore = defineStore('institution', {
  state: (): InstitutionState => ({
    dashboardData: {
      currentStatus: FORM_STATUS.SUBMITTED,
      lastUpdatedDate: "2025-12-18",
      isNOCCompleted: false,
      trackData: [
        {
          object: 'Form 1',
          date: '2024-06-01',
          status: 'Done'
        },
          {
          object: 'Form 2',
          date: '2024-06-01',
          status: 'Pending'
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
        this.dashboardData = { ...response }
      } catch (err: any) {
        this.status = 'failed'
        this.error = err?.response?.data?.message || err?.message || 'Unable to fetch dashboard data'
      }
    },
  },
})

export default useInstitutionStore

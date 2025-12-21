import { defineStore } from 'pinia'
import type { Status } from '@/types/common'
import { getDashboardData } from '@/modules/department/services/department.service'

export interface DepartmentState {
  dashboardData: {
    totalPendingApplication: number,
    totalInProcessApplication: number,
    totalNocCompleteApplication: number,
  }
  status: Status
  error: string | null
}

export const useDepartmentStore = defineStore('department', {
  state: (): DepartmentState => ({
    dashboardData: {
      totalPendingApplication: 0,
      totalInProcessApplication: 0,
      totalNocCompleteApplication: 0,
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

export default useDepartmentStore

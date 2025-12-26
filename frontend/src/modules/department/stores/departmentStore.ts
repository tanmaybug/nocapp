import { defineStore } from 'pinia'
import { STATUS, type Status } from '@/types/common'
import { getDashboardData, getNOCApplicationsByStatus } from '@/modules/department/services/department.service'

export const NOC_APPLICATION_TYPE = {
  PENDING: 'pending',
  IN_PROCESS: 'in-process',
  COMPLETED: 'completed',
} as const
export type NOCApplicationType = typeof NOC_APPLICATION_TYPE[keyof typeof NOC_APPLICATION_TYPE]

export type NOCApplication = {
  registrationId: string
  institutionName: string
  applicantName: string
  applicantPhone: string
  applicantEmail: string
}

export type DepartmentState = {
  dashboardData: {
    totalPendingApplication: number,
    totalInProcessApplication: number,
    totalNocCompleteApplication: number,
    status: Status,
    error: string | null
  }
  nocApplications: {
    type: NOCApplicationType
    nocApplications: NOCApplication[]
    status: Status
    error: string | null
  }
}

export const useDepartmentStore = defineStore('department', {
  state: (): DepartmentState => ({
    dashboardData: {
      totalPendingApplication: 0,
      totalInProcessApplication: 0,
      totalNocCompleteApplication: 0,
      status: STATUS.INITIALIZED,
      error: null,
    },
    nocApplications: {
      type: NOC_APPLICATION_TYPE.PENDING,
      nocApplications: [],
      status: STATUS.INITIALIZED,
      error: null,
    },
  }),
  actions: {
    async getDashboardData(): Promise<void> {
      this.dashboardData = {
        ...this.dashboardData,
        totalPendingApplication: 0,
        totalInProcessApplication: 0,
        totalNocCompleteApplication: 0,
        status: STATUS.INITIALIZED,
        error: null,
      }
      try {
        const { data } = await getDashboardData()
        this.dashboardData = { ...this.dashboardData, ...data, status: STATUS.PROCESSED }
      } catch (err: any) {
        this.dashboardData = {
          ...this.dashboardData,
          status: STATUS.FAILED,
          error: err?.response?.data?.message || err?.message || 'Unable to fetch dashboard data'
        }
      }
    },
    async getNOCApplicationsByStatus(nocApplicationType: NOCApplicationType): Promise<void> { 
      this.nocApplications = {
        ...this.nocApplications,
        type: nocApplicationType,
        nocApplications: [],
        status: STATUS.INITIALIZED,
        error: null,
      }
      try {
        const {data} = await getNOCApplicationsByStatus(nocApplicationType)
        this.nocApplications = { 
          ...this.nocApplications,
          nocApplications: data,
          status: STATUS.PROCESSED
         }
      } catch (err: any) {
        this.nocApplications = {
          ...this.nocApplications,
          status: STATUS.FAILED,
          error: err?.response?.data?.message || err?.message || 'Unable to fetch NOC applications'
        }
      }
    },
  },
})

export default useDepartmentStore

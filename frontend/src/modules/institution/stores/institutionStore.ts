import { defineStore } from 'pinia'
import type { Status } from '@/types/common'
import { getDashboardData, getNOCApplicationView, getTrackApplication } from '@/modules/institution/services/institution.service'

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
export type TrackActivity = {
  sno: number
  activity: string
  date: string
  remarks: string
}

export type NOCApplicationView = {
  applicantDetails: {
    entityType: string
    applicantName: string
    isMinority: string
    minorityType: string
    language: string
    religion: string
    applicationId: string
    applicantMobileNo: number | string
    applicantEmailId: string
    applicantTanNo: string
    applicantLocation: {
      applicantAddress: string
      district: string
      subDivision: string
      policeStation: string
      postOffice: string
      municipalityBlock: string
      city: string
      pin: number | string
    }
  }
  collegeDetails: {
    proposedCollegeName: string
    affiliatedUniversity: string
    institutionFor: string
    collegeLocation: {
      collegeAddress: string
      districtId: string
      subDivisionId: string
      policeStation: string
      postOffice: string
      gramPanchayat: string
      municipalityBlock: string
      pin: number | string
    }
  }
  institutionPurpose: {
    aimAndObjective: {
      vision: string
      mission: string
      coreValues: string
      aims: string
      objectiveConcernedInstitution: string
    }
    collegeLandDetails: {
      mouza: string
      jlNo: string
      khatianNo: string
      plotNo: string
      areaClasification: number | string
    }
    credibilityAndReadiness: {
      experienceInEducation: string
      generalReputation: string
      readinessToComplyWithRegulatoryNorms: string
    }
    additionalCommitmentsAndPlans: {
      studentReservation: number | null
      employeeReservation: number | null
      specialSkillDevelopmentActivity: number | null
      academicAuditingPlans: number | null
    }
  }
  campusDevelopment: {
    campusDevlopmentPlan: {
      approvedPlanWith: {
        totalBuildUpArea: number | string
        groundFloorArea: number | string
        firstFloorArea: number | string
      }
      totalNumberOf: {
        classRoomCount: number | string
        seminarRoomCount: number | string
        multipurposeHallCount: number | string
        labResourceCenterCount: number | string
        ictEduTechLabCount: number | string
        languageLabCount: number | string
        storeRoomCount: number | string
        boysCommonRoomCount: number | string
        girlsCommonRoomCount: number | string
        boysToiletCount: number | string
        girlsToiletCount: number | string
      }
      anyOtherRoom: {
        conferrenceRoomStatus: number | null
        meetingRoomStatus: number | null
      }
      libraryDetails: {
        totalSpace: number | string
        readingRoomCount: number | string
        booksCount: number | string
        journalPeriodicalCount: number | string
      }
      administrativeOfficeStatus: number | null
      totalPlannedConstruction: number | string
    }
    comprehensivePlan: string
    collegeLandAreaInAcres: number | string
    collegeCoveredArea: number | string
    landStatus: {
      landOwnedStatus: number | null
      landConvertedForEducationalPurposeStatus: number | null
    }
  }
  financialDetails: {
    projectedFundFlow: { amount: string; sourceOfFund: string }
    synopsis: {
      proposedInvestment: string
      proposedEmployment: string
      professionalCollegesCountWithin25Km: string
      feederSchoolCountWithin15Km: string
    }
    buildingCompletionStatus: string
    buildingCompletionDate: string
    buildingCompletionExpectedDate: string
    buildingPlanAmountToBeDeposited: string
    estimatedIncomeAndExpenditureForFirst5Years: string
    initialFundInformation: string
    nationalizedBank: string
  }
  documentData: Array<{
    fieldName: string
    label: string
    filePath: string | null
  }>
  logoPath: string
}

export type InstitutionStoreState = {
  dashboardData: {
    currentStatus: string | null
    lastUpdatedDate: String | null
    inspectionDate: string | null
    isNOCCompleted: boolean
    activities: Activity[]
  }
  trackApplication: TrackActivity[]
  nocApplicationView: NOCApplicationView | null
  status: Status
  error: string | null
}

export const useInstitutionStore = defineStore('institution', {
  state: (): InstitutionStoreState => ({
    dashboardData: {
      currentStatus: null,
      lastUpdatedDate: null,
      inspectionDate: null,
      isNOCCompleted: false,
      activities: []
    },
    trackApplication: [],
    nocApplicationView: null,
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
    async getTrackApplication(): Promise<void> {
      this.status = 'processing'
      this.error = null
      try {
        const response = await getTrackApplication()
        this.trackApplication = response.data ?? []
        this.status = 'processed'
      } catch (err: any) {
        this.status = 'failed'
        this.error = err?.response?.data?.message || err?.message || 'Unable to fetch track application data'
      }
    },
    async getNOCApplicationView(): Promise<void> {
      this.status = 'processing'
      this.error = null
      try {
        const response = await getNOCApplicationView()
        this.nocApplicationView = response.data ?? null
        this.status = 'processed'
      } catch (err: any) {
        this.status = 'failed'
        this.error = err?.response?.data?.message || err?.message || 'Unable to fetch NOC application data'
      }
    },
  },
})

export default useInstitutionStore

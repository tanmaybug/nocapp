import { defineStore } from 'pinia'
import type { Status } from '@/types/common'
import useDialogStore from './dialogStore'
import { submitNocForm } from '@/apis'

export type NOCFormType = 'form1' | 'form2' | 'form3'

type Nullable<T> = T | null

interface Form1Data {
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
    areaClasification: Nullable<number>
  }
  collegeLandAreaInAcres: string
  collegeCoveredArea: string
  credibilityAndReadiness: {
    experienceInEducation: string
    generalReputation: string
    readinessToComplyWithRegulatoryNorms: string
  }
  additionalCommitmentsAndPlans: {
    studentReservation: Nullable<number>
    employeeReservation: Nullable<number>
    specialSkillDevelomentActivity: Nullable<number>
    academicAuditingPlans: Nullable<number>
  }
  landStatus: {
    landOwnedStatus: Nullable<number>
    landConvertedForEducationalPurposeStatus: Nullable<number>
  }
  comprehensivePlan: string
  campusDevlopmentPlan: {
    approvedPlanWith: {
      totalBuildUpArea: string
      groundFloorArea: string
      firstFloorArea: string
    }
    totalNumberOf: {
      classRoomCount: string
      seminarRoomCount: string
      multipurposeHallCount: string
      labResourceCenterCount: string
      ictEduTechLabCount: string
      languageLabCount: string
      storeRoomCount: string
      boysCommonRoomCount: string
      girlsCommonRoomCount: string
      boysToiletCount: string
      girlsToiletCount: string
    }
    anyOtherRoom: {
      conferrenceRoomStatus: Nullable<number>
      meetingRoomStatus: Nullable<number>
    }
    libraryDetails: {
      totalSpace: string
      readingRoomCount: string
      booksCount: string
      journalPeriodicalCount: string
    }
    administrativeOfficeStatus: Nullable<number>
    totalPlannedConstruction: string
  }
}

interface Form2Data {
  projectedFundFlow: {
    amount: string
    sourceOfFund: string
  }
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

interface Form3Data {
  proposalForCampusDevelopmentProgram: Array<string | number>
  experienceAndExpertiseInDiscipline: Array<string | number>
  feeStructureProposal: Array<string | number>
  endowmentFundDetails: Array<string | number>
  employeeAppointmentProcedure: Array<string | number>
  extracurricularActivitiesAndPlacesDetails: Array<string | number>
  societyRegistrationCertificate: Array<string | number>
  conveyanceDeed: Array<string | number>
  homesteadPurposeConversionApplication: Array<string | number>
  gripsEchallan: Array<string | number>
  buildingPlan: Array<string | number>
  proofoFFees: Array<string | number>
  proofOfLand: Array<string | number>
  phasedDevlopmentBluePrint: Array<string | number>
  prrofOfContiguousLandOwnership: Array<string | number>
  otherInformation: Array<string | number>
}

interface NOCForm {
  form1: Form1Data
  form2: Form2Data
  form3: Form3Data
}

interface NOCStoreState {
  status: Status
  error: string | null
  form: NOCForm
  submissionProgress: Record<NOCFormType, boolean>
  dialogStore: ReturnType<typeof useDialogStore>
}

export const NOC_FORM_LABEL_MAP: Record<NOCFormType, string> = {
  form1: 'General Information',
  form2: 'Funding & Investment',
  form3: 'Document Upload'
} as const

function createDefaultNOCData(): NOCForm {
  return {
    form1: {
      aimAndObjective: {
        vision: '',
        mission: '',
        coreValues: '',
        aims: '',
        objectiveConcernedInstitution: ''
      },
      collegeLandDetails: {
        mouza: '',
        jlNo: '',
        khatianNo: '',
        plotNo: '',
        areaClasification: null
      },
      collegeLandAreaInAcres: '',
      collegeCoveredArea: '',
      credibilityAndReadiness: {
        experienceInEducation: '',
        generalReputation: '',
        readinessToComplyWithRegulatoryNorms: ''
      },
      additionalCommitmentsAndPlans: {
        studentReservation: null,
        employeeReservation: null,
        specialSkillDevelomentActivity: null,
        academicAuditingPlans: null
      },
      landStatus: {
        landOwnedStatus: null,
        landConvertedForEducationalPurposeStatus: null,
      },
      comprehensivePlan: '',
      campusDevlopmentPlan: {
        approvedPlanWith: {
          totalBuildUpArea: '',
          groundFloorArea: '',
          firstFloorArea: ''
        },
        totalNumberOf: {
          classRoomCount: '',
          seminarRoomCount: '',
          multipurposeHallCount: '',
          labResourceCenterCount: '',
          ictEduTechLabCount: '',
          languageLabCount: '',
          storeRoomCount: '',
          boysCommonRoomCount: '',
          girlsCommonRoomCount: '',
          boysToiletCount: '',
          girlsToiletCount: ''
        },
        anyOtherRoom: {
          conferrenceRoomStatus: null,
          meetingRoomStatus: null
        },
        libraryDetails: {
          totalSpace: '',
          readingRoomCount: '',
          booksCount: '',
          journalPeriodicalCount: ''
        },
        administrativeOfficeStatus: null,
        totalPlannedConstruction: ''
      }
    },
    form2: {
      projectedFundFlow: {
        amount: '',
        sourceOfFund: ''
      },
      synopsis: {
        proposedInvestment: '',
        proposedEmployment: '',
        professionalCollegesCountWithin25Km: '',
        feederSchoolCountWithin15Km: ''
      },
      buildingCompletionStatus: '',
      buildingCompletionDate: '',
      buildingCompletionExpectedDate: '',
      buildingPlanAmountToBeDeposited: '',
      estimatedIncomeAndExpenditureForFirst5Years: '',
      initialFundInformation: '',
      nationalizedBank: ''
    },
    form3: {
      proposalForCampusDevelopmentProgram: [],
      experienceAndExpertiseInDiscipline: [],
      feeStructureProposal: [],
      endowmentFundDetails: [],
      employeeAppointmentProcedure: [],
      extracurricularActivitiesAndPlacesDetails: [],
      societyRegistrationCertificate: [],
      conveyanceDeed: [],
      homesteadPurposeConversionApplication: [],
      gripsEchallan: [],
      buildingPlan: [],
      proofoFFees: [],
      proofOfLand: [],
      phasedDevlopmentBluePrint: [],
      prrofOfContiguousLandOwnership: [],
      otherInformation: []
    }
  }
}

export const useNOCStore = defineStore('noc', {
  state: (): NOCStoreState => ({
    status: 'initialized',
    error: null,
    form: createDefaultNOCData(),
    submissionProgress: {
      form1: false,
      form2: false,
      form3: false
    },
    dialogStore: useDialogStore()
  }),

  getters: {
    isTabSubmitted: (state: NOCStoreState) => (tabKey: NOCFormType): boolean => {
      return state.submissionProgress[tabKey] || false
    },

    allTabsSubmitted: (state: NOCStoreState): boolean => {
      return Object.values(state.submissionProgress).every(submitted => submitted)
    },

    getTabData: (state: NOCStoreState) => <T extends NOCFormType>(tabKey: T): NOCForm[T] => {
      return state.form[tabKey]
    }
  },

  actions: {
    updateTabData<T extends NOCFormType>(tabKey: T, data: NOCForm[T]): void {
      this.form[tabKey] = data
    },

    async submitTab<T extends NOCFormType>(tabKey: T): Promise<void> {
      this.status = 'processing'
      this.error = null

      try {
        const data = this.form[tabKey]

        await submitNocForm(tabKey, { ...data } )

        // Mark tab as submitted
        this.submissionProgress[tabKey] = true

        this.status = 'processed'
        this.dialogStore.showDialog({
          type: 'ALERT',
          title: 'Tab Submitted',
          message: `${NOC_FORM_LABEL_MAP[tabKey]} has been submitted successfully!`
        })

        // If all tabs are submitted, show final completion message
        if (this.allTabsSubmitted) {
          this.dialogStore.showDialog({
            type: 'ALERT',
            title: 'NOC Application Complete',
            message: 'All sections have been submitted successfully!'
          })
        }

      } catch (err: any) {
        this.status = 'failed'
        this.error = err?.response?.data?.message || err?.message || 'Submission failed'
        this.dialogStore.showDialog({
          type: 'ALERT',
          title: 'Submission Failed',
          message: this.error!
        })
        throw err
      }
    },

    async submitCompleteForm(): Promise<void> {
      this.status = 'processing'
      this.error = null

      try {
        // Submit complete form - only if all tabs are submitted
        if (!this.allTabsSubmitted) {
          throw new Error('Please submit all tabs before final submission')
        }

        // Simulate API call for complete form submission
        // Replace with actual API call: await submitCompleteNOC(this.form)
        await new Promise((resolve) => setTimeout(resolve, 2000))

        this.status = 'processed'
        this.dialogStore.showDialog({
          type: 'ALERT',
          title: 'NOC Application Submitted',
          message: 'Your complete NOC application has been submitted successfully!'
        })

      } catch (err: any) {
        this.status = 'failed'
        this.error = err?.response?.data?.message || err?.message || 'Final submission failed'
        this.dialogStore.showDialog({
          type: 'ALERT',
          title: 'Submission Failed',
          message: this.error!
        })
        throw err
      }
    }
  }
})

export default useNOCStore

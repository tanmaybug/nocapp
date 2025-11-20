import { defineStore } from 'pinia'
import type { Status } from '@/types/common'
import useDialogStore from './dialogStore'

function createDefaultNOCData() {
  return {
    generalInformation: {
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
      landOwnedStatus: null,
      landConvertedForEducationalPurposeStatus: null,
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
    fundingData: {
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
    documentData: {
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
  state: (): {
    status: Status
    error: string | null
    form: any
    submissionProgress: {
      generalInformation: boolean
      fundingData: boolean
      documentData: boolean
    }
    dialogStore: ReturnType<typeof useDialogStore>
  } => ({
    status: 'initialized',
    error: null,
    form: createDefaultNOCData(),
    submissionProgress: {
      generalInformation: false,
      fundingData: false,
      documentData: false
    },
    dialogStore: useDialogStore()
  }),
  
  getters: {
    isTabSubmitted: (state) => (tabKey: string) => {
      return (state.submissionProgress as any)[tabKey] || false
    },
    
    allTabsSubmitted: (state) => {
      return Object.values(state.submissionProgress).every(submitted => submitted)
    },
    
    getTabData: (state) => (tabKey: string) => {
      return (state.form as any)[tabKey]
    }
  },
  
  actions: {
    updateTabData(tabKey: string, data: any) {
      if (tabKey in this.form) {
        (this.form as any)[tabKey] = data
      }
    },
    
    async submitTab(tabKey: string, tabData: any) {
      this.status = 'processing'
      this.error = null
      
      try {
        // Update the form data
        this.updateTabData(tabKey, tabData)
        
        // Simulate API call for tab submission
        // Replace with actual API call: await submitNOCTab(tabKey, tabData)
        await new Promise((resolve) => setTimeout(resolve, 1000))
        
        // Mark tab as submitted
        ;(this.submissionProgress as any)[tabKey] = true
        
        this.status = 'processed'
        this.dialogStore.showDialog({
          type: 'ALERT',
          title: 'Tab Submitted',
          message: `${this.getTabDisplayName(tabKey)} has been submitted successfully!`
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
    
    async submitCompleteForm() {
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
    },
    
    getTabDisplayName(tabKey: string): string {
      const displayNames: Record<string, string> = {
        generalInformation: 'General Information',
        fundingData: 'Funding & Investment',
        documentData: 'Document Upload'
      }
      return displayNames[tabKey] || tabKey
    }
  }
})

export default useNOCStore

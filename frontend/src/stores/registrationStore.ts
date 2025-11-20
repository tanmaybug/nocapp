import { defineStore } from 'pinia'
import type { Status } from '@/types/common'
import { submitRegistration, getRegistrationFormOptions, getPostOffices, getGramPanchayats } from '@/apis'
import { filterProperties } from '@/composables/helpers'
import useDialogStore from './dialogStore'

function createDefaultRegistrationData() {
  return {
    entityTypeID: null,
    applicantName: '',
    isRegistered: null,
    registrationNo: '',
    registrationDate: '',
    placeOfRegistration: '',
    minorityTypeId: null,
    minorityFlag: null,
    minorityDetails: '',    
    applicantLocation: {
      applicantAddress: '',
      districtId: null,
      subDivisionId: null,
      policeStationId: null,
      postOfficeId: null,
      assemblyConstituencyId: null,
      municipalityBlockId: null,
      city: '',
      pin: '',
    },
    proposedCollegeName: '',
    affiliatedUniversityId: null,
    institutionForId: null,
    collegeLocation: {
      collegeAddress: '',
      districtId: null,
      subDivisionId: null,
      policeStationId: null,
      postOfficeId: null,
      gramPanchayatId: null,
      assemblyConstituencyId: null,
      municipalityBlockId: null,
      pin: '',
    },
    applicantMobileNo: '',
    applicantTanNo: '',
    applicantEmailId: '',
    password: ''
  }
}

export const useRegistrationStore = defineStore('registration', {
  state: (): {
    entityTypes: any[],
    minorityTypes: any[],
    districts: any[],
    subDivisions: any[],
    policeStations: any[],
    applicantPostOffices: any[],
    collegePostOffices: any[],
    municipalityBlocks: any[],
    assemblyConstituencies: any[],
    gramPanchayats: any[],
    instituteType: any[],
    affiliatedUniversities: any[],
    status: Status
    error: string | null
    form: any
    dialogStore: ReturnType<typeof useDialogStore>
  } => ({
    entityTypes: [],
    minorityTypes: [],
    districts: [],
    subDivisions: [],
    policeStations: [],
    applicantPostOffices: [],
    collegePostOffices: [],
    municipalityBlocks: [],
    assemblyConstituencies: [],
    gramPanchayats: [],
    instituteType: [],
    affiliatedUniversities: [],
    status: 'initialized',
    error: null,
    form: createDefaultRegistrationData(),
    dialogStore: useDialogStore()
  }),
  actions: {
    async getFormOptions() {
      try {
        const response = await getRegistrationFormOptions()
        const optionFields = filterProperties(response.data, [
            'entityTypes',
            'minorityTypes',
            'districts',
            'subDivisions',
            'policeStations',
            'municipalityBlocks',
            'assemblyConstituencies',
            'instituteType',
            'affiliatedUniversities'
          ])

        Object.keys(optionFields).forEach((key) => {
          const k = key as keyof typeof optionFields
          if (k in this.$state) {
            (this.$state as any)[k] = (optionFields as any)[k]
          }
        })
      } catch (e) {
        this.error = 'Error in fetching form options'
      }
    },
    async getPostOffices(type: 'applicant' | 'college', pin: number) {
      try {
        const response = await getPostOffices(pin)
        this[`${type}PostOffices`] = response.data.postOffices
      } catch (e) {
        this.error = 'Error in fetching post offices'
      }
    },
    async getGramPanchayats(municipalityBlockId: number) {
      try {
        const response = await getGramPanchayats(municipalityBlockId)
        this.gramPanchayats = response.data.gramPanchayats
      } catch (e) {
        this.error = 'Error in fetching gram panchayats'
      }
    },
    resetForm() {
      this.form = createDefaultRegistrationData()
    },
    
    async submitRegistration() {
      this.status = 'processing'
      this.error = null
      try {
        const response =await submitRegistration({ ...this.form, confirm_password: this.form.password })
        alert(response.data.noc_registration_id)
        this.status = 'processed'
        this.dialogStore.showDialog({ type: 'ALERT', title: 'Registration Successful', message: `Your registration ID is ${response.data.noc_registration_id}`})
      } catch (err: any) {
        this.status = 'failed'
        this.error = err?.response?.data?.message || err?.message || 'Registration failed'
        this.dialogStore.showDialog({ type: 'ALERT', title: 'Registration Failed', message: this.error! })
        throw err
      }
    }
  },
})

export default useRegistrationStore

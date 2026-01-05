<template>
  <v-row class="pa-2 pt-5">
    <v-col cols="12" v-for="(field, fieldKey) in fileUploadFields" :key="fieldKey">
      <FileUploadField :label="field.label" v-model:uploadedFiles="uploadedFiles[fieldKey].value" :rules="[]" :documentId="field.documentId" />
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { ref, watch, reactive } from 'vue'
import type { PropType } from 'vue'
import FileUploadField from '@/components/ui/FileUploadField.vue'

// Props
type ModelValue = {
  proposalForCampusDevelopmentProgram: any[]
  experienceAndExpertiseInDiscipline: any[]
  feeStructureProposal: any[]
  endowmentFundDetails: any[]
  employeeAppointmentProcedure: any[]
  extracurricularActivitiesAndPlacesDetails: any[]
  societyRegistrationCertificate: any[]
  conveyanceDeed: any[]
  gripsEchallan: any[]
  buildingPlan: any[]
  proofOfFees: any[]
  proofOfLand: any[]
  phasedDevelopmentBluePrint: any[]
  proofOfContiguousLandOwnership: any[]
  otherInformation: any[]
}

const { modelValue } = defineProps({
  modelValue: { type: Object as PropType<ModelValue>, required: true },
})

// Emits
const emit = defineEmits<{
  'update:modelValue': [value: any]
}>()

// Configuration
const fileUploadFields = {
  proposalForCampusDevelopmentProgram: {
    label: 'Proposal for campus development programme to be undertaken during first five years in phased manner after commencement of functioning of the self-financing college and phased outlays of capital expenditure and sources of finance for those five years',
    displayName: 'Proposal for campus development',
    required: false,
    documentId: 1
  },
  experienceAndExpertiseInDiscipline: {
    label: 'The experience and expertise in the concerned discipline',
    displayName: 'Experience and expertise',
    required: false,
    documentId: 2
  },
  feeStructureProposal: {
    label: 'Details of proposed fee structure along with proposal of fee concession/fee exemption for the poor and physically handicapped students',
    displayName: 'Fee structure proposal',
    required: false,
    documentId: 3
  },
  endowmentFundDetails: {
    label: 'Details of Endowment Fund',
    displayName: 'Endowment fund details',
    required: false,
    documentId: 4
  },
  employeeAppointmentProcedure: {
    label: 'Procedure to be followed for appointment of officials having requisite qualifications as well as non-teaching staff for the proposed college',
    displayName: 'Employee appointment procedure',
    required: false,
    documentId: 5
  },
  extracurricularActivitiesAndPlacesDetails: {
    label: 'Details of playground, auditorium and other facilities available or proposed to be created for games, sports, culture and extracurricular activities like NSS, NCC, Scouts and Guides etc',
    displayName: 'Extracurricular activities details',
    required: false,
    documentId: 6
  },
  societyRegistrationCertificate: {
    label: 'Certificate of Registration of Societies West Bengal ACT XXVI of 1961',
    displayName: 'Society registration certificate',
    required: false,
    documentId: 7
  },
  conveyanceDeed: {
    label: 'Deed of Conveyance',
    displayName: 'Conveyance deed',
    required: false,
    documentId: 8
  },
  gripsEchallan: {
    label: 'Govt of West Bengal Land & Land Reforms GRIPS eChallan',
    displayName: 'GRIPS eChallan',
    required: false,
    documentId: 10
  },
  buildingPlan: {
    label: 'Building Plan',
    displayName: 'Building plan',
    required: false,
    documentId: 11
  },
  proofOfFees: {
    label: 'Upload the proof of fees structure',
    displayName: 'Proof of fees',
    required: false,
    documentId: 12
  },
  proofOfLand: {
    label: 'Upload the document for the proof of land',
    displayName: 'Proof of land',
    required: false,
    documentId: 13
  },
  phasedDevelopmentBluePrint: {
    label: 'Upload the Blue-print for phased development',
    displayName: 'Phased development blueprint',
    required: false,
    documentId: 14
  },
  proofOfContiguousLandOwnership: {
    label: 'Upload the proof of the contiguous land ownership',
    displayName: 'Proof of contiguous land ownership',
    required: false,
    documentId: 15
  },
  otherInformation: {
    label: 'Any other information that the applicant may like to share',
    displayName: 'Other information',
    required: false,
    documentId: 16
  }
}

// State
const uploadedFiles = reactive(Object.keys(fileUploadFields).reduce((acc, key) => {
  acc[key] = ref<any[]>([])
  return acc
}, {} as Record<string, any>))

// Keep modelValue in sync (if the API needs file ids in payload)
Object.keys(fileUploadFields).forEach((fieldKey) => {
  watch(uploadedFiles[fieldKey], (newDocs: any[]) => {
    modelValue[fieldKey as keyof ModelValue] = (newDocs || [])
      .map((doc: any) => doc?.fileId ?? doc?.id)
      .filter(Boolean)
    emit('update:modelValue', modelValue)
  }, { deep: true })
})
</script>

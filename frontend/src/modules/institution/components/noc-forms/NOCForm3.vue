<template>
  <v-row class="pa-2 pt-5">
    <v-col cols="12" v-for="(field, fieldKey) in fileUploadFields" :key="fieldKey">
      <FileUploadField :label="field.label" :uploadedFiles="uploadedFiles[fieldKey].value" :rules="[]" @add="onAddForField(fieldKey, field.displayName, $event)" @remove="onRemoveForField(fieldKey, $event)" />
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { ref, watch, reactive } from 'vue'
import FileUploadField from '@/components/ui/FileUploadField.vue'
import { useFileStore } from '@/stores/fileStore'

// Props
const props = defineProps<{
  modelValue: {
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
}>()

// Emits
const emit = defineEmits<{
  'update:modelValue': [value: any]
}>()

// Stores / base state
const fileStore = useFileStore()

// Configuration
const fileUploadFields = {
  proposalForCampusDevelopmentProgram: {
    label: 'Proposal for campus development programme to be undertaken during first five years in phased manner after commencement of functioning of the self-financing college and phased outlays of capital expenditure and sources of finance for those five years',
    displayName: 'Proposal for campus development',
    required: false
  },
  experienceAndExpertiseInDiscipline: {
    label: 'The experience and expertise in the concerned discipline',
    displayName: 'Experience and expertise',
    required: false
  },
  feeStructureProposal: {
    label: 'Details of proposed fee structure along with proposal of fee concession/fee exemption for the poor and physically handicapped students',
    displayName: 'Fee structure proposal',
    required: false
  },
  endowmentFundDetails: {
    label: 'Details of Endowment Fund',
    displayName: 'Endowment fund details',
    required: false
  },
  employeeAppointmentProcedure: {
    label: 'Procedure to be followed for appointment of officials having requisite qualifications as well as non-teaching staff for the proposed college',
    displayName: 'Employee appointment procedure',
    required: false
  },
  extracurricularActivitiesAndPlacesDetails: {
    label: 'Details of playground, auditorium and other facilities available or proposed to be created for games, sports, culture and extracurricular activities like NSS, NCC, Scouts and Guides etc',
    displayName: 'Extracurricular activities details',
    required: false
  },
  societyRegistrationCertificate: {
    label: 'Certificate of Registration of Societies West Bengal ACT XXVI of 1961',
    displayName: 'Society registration certificate',
    required: false
  },
  conveyanceDeed: {
    label: 'Deed of Conveyance',
    displayName: 'Conveyance deed',
    required: false
  },
  gripsEchallan: {
    label: 'Govt of West Bengal Land & Land Reforms GRIPS eChallan',
    displayName: 'GRIPS eChallan',
    required: false
  },
  buildingPlan: {
    label: 'Building Plan',
    displayName: 'Building plan',
    required: false
  },
  proofOfFees: {
    label: 'Upload the proof of fees structure',
    displayName: 'Proof of fees',
    required: false
  },
  proofOfLand: {
    label: 'Upload the document for the proof of land',
    displayName: 'Proof of land',
    required: false
  },
  phasedDevelopmentBluePrint: {
    label: 'Upload the Blue-print for phased development',
    displayName: 'Phased development blueprint',
    required: false
  },
  proofOfContiguousLandOwnership: {
    label: 'Upload the proof of the contiguous land ownership',
    displayName: 'Proof of contiguous land ownership',
    required: false
  },
  otherInformation: {
    label: 'Any other information that the applicant may like to share',
    displayName: 'Other information',
    required: false
  }
}

// State
const uploadedFiles = reactive(Object.keys(fileUploadFields).reduce((acc, key) => {
  acc[key] = ref<any[]>([])
  return acc
}, {} as Record<string, any>))

// Handlers
function onAddForField(fieldKey: string, displayName: string, file: File | null) {
  return uploadFile(file, uploadedFiles[fieldKey], displayName)
}
function onRemoveForField(fieldKey: string, index: number) {
  return removeItem(uploadedFiles[fieldKey], index)
}

// Helpers
async function uploadFile(file: File | null, uploadedArrayRef: any, label?: string) {
  if (!file) return

  const fd = new FormData()
  fd.append('file', file as Blob, (file as any).name)

  try {
    const resp: any = await fileStore.uploadFile(fd)
    uploadedArrayRef.value.push(resp[0])
  } catch (err: any) {
    console.error(`${label || 'File'} upload failed`, err)
  }
}

// Generic remover function
function removeItem(collection: any, index: number, options?: { minLength?: number }) {
  const minLength = options?.minLength ?? 0
  const arr = collection?.value ?? collection
  if (!Array.isArray(arr)) return
  if (index < 0 || index >= arr.length) return
  if (arr.length < minLength) return
  arr.splice(index, 1)
}

// Watchers
Object.keys(fileUploadFields).forEach(fieldKey => {
  watch(uploadedFiles[fieldKey], (newDocs: any[]) => {
    props.modelValue[fieldKey as keyof typeof props.modelValue] = newDocs.map((doc: any) => doc.id)
    emit('update:modelValue', props.modelValue)
  }, { deep: true })
})
</script>

<template>
  <v-row class="pa-2">
    <v-col cols="12">
      <v-alert type="info" variant="tonal" class="mt-4">
        <div class="ml-2">
          <strong>File Upload Guidelines:</strong>
          <ul class="mt-2">
            <li>Accepted formats: PDF, DOC, DOCX, JPG, JPEG, PNG</li>
            <li>Maximum file size: 10MB per file</li>
            <li>All fields are optional</li>
            <li>Ensure documents are clear and legible</li>
          </ul>
        </div>
      </v-alert>
    </v-col>

    <v-col cols="12" v-for="(field, fieldKey) in fileUploadFields" :key="fieldKey">
      <FileUploadField :label="field.label" :uploadedFiles="uploadedFiles[fieldKey]" :rules="[]" @add="(file) => uploadFile(file, uploadedFiles[fieldKey], field.displayName)" @remove="(index) => removeItem(uploadedFiles[fieldKey], index)" />
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { ref, watch, reactive } from 'vue'
import FileUploadField from '@/components/FileUploadField.vue'
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
    proofoFFees: any[]
    proofOfLand: any[]
    phasedDevlopmentBluePrint: any[]
    prrofOfContiguousLandOwnership: any[]
    otherInformation: any[]
  }
}>()

// Emits
const emit = defineEmits<{
  'update:modelValue': [value: any]
}>()

const fileStore = useFileStore()

// Configuration for all file upload fields
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
  proofoFFees: {
    label: 'Upload the proof of fees structure',
    displayName: 'Proof of fees',
    required: false
  },
  proofOfLand: {
    label: 'Upload the document for the proof of land',
    displayName: 'Proof of land',
    required: false
  },
  phasedDevlopmentBluePrint: {
    label: 'Upload the Blue-print for phased development',
    displayName: 'Phased development blueprint',
    required: false
  },
  prrofOfContiguousLandOwnership: {
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

// Create reactive uploaded files object
const uploadedFiles = reactive(Object.keys(fileUploadFields).reduce((acc, key) => {
  acc[key] = ref<any[]>([])
  return acc
}, {} as Record<string, any>))

// Upload helper function
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

// Watchers to update modelValue when files change
Object.keys(fileUploadFields).forEach(fieldKey => {
  watch(uploadedFiles[fieldKey], (newDocs: any[]) => {
    props.modelValue[fieldKey as keyof typeof props.modelValue] = newDocs.map((doc: any) => doc.id)
    emit('update:modelValue', props.modelValue)
  }, { deep: true })
})
</script>

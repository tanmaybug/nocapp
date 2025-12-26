<template>
  <v-row class="pa-2">
    <!-- Aims and objectives of the proposed self-financing UG college -->
    <v-col cols="12">
      <div class="text-subtitle-1"><strong>Aims and objectives of the proposed self-financing UG college</strong></div>
    </v-col>

    <v-col cols="6">
      <v-text-field v-model="modelValue.aimAndObjective.vision" label="Vision" @input="updateValue" />
    </v-col>

    <v-col cols="6">
      <FileUploadField :label="'Vision Files'" :uploadedFiles="uploadedVisionFiles" :rules="[]" @add="onAddVision" @remove="onRemoveVision" />
    </v-col>

    <v-col cols="6">
      <v-text-field v-model="modelValue.aimAndObjective.mission" label="Mission" @input="updateValue" />
    </v-col>

    <v-col cols="6">
      <FileUploadField :label="'Mission Files'" :uploadedFiles="uploadedMissionFiles" :rules="[]" @add="onAddMission" @remove="onRemoveMission" />
    </v-col>

    <v-col cols="6">
      <v-text-field v-model="modelValue.aimAndObjective.coreValues" label="Core Values" @input="updateValue" />
    </v-col>

    <v-col cols="6">
      <FileUploadField :label="'Core Values Files'" :uploadedFiles="uploadedCoreValuesFiles" :rules="[]" @add="onAddCoreValues" @remove="onRemoveCoreValues" />
    </v-col>

    <v-col cols="6">
      <v-text-field v-model="modelValue.aimAndObjective.aims" label="Aims" @input="updateValue" />
    </v-col>

    <v-col cols="6">
      <FileUploadField :label="'Aims Files'" :uploadedFiles="uploadedAimsFiles" :rules="[]" @add="onAddAims" @remove="onRemoveAims" />
    </v-col>

    <v-col cols="6">
      <v-text-field v-model="modelValue.aimAndObjective.objectiveConcernedInstitution" label="Objectives of Concerned Institution" @input="updateValue" />
    </v-col>

    <v-col cols="6">
      <FileUploadField :label="'Objectives of Concerned Institution Files'" :uploadedFiles="uploadedObjectiveConcernedInstitutionFiles" :rules="[]" @add="onAddObjectiveConcernedInstitution" @remove="onRemoveObjectiveConcernedInstitution" />
    </v-col>

    <!-- Details of the land of the college -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="12">
      <div class="text-subtitle-1"><strong>Details of the land of the college</strong></div>
    </v-col>

    <v-col cols="6">
      <v-text-field v-model="modelValue.collegeLandDetails.mouza" label="Mouza" @input="updateValue" />
    </v-col>

    <v-col cols="6">
      <v-text-field v-model="modelValue.collegeLandDetails.jlNo" label="JL No" @input="updateValue" />
    </v-col>

    <v-col cols="2">
      <div class="text-body-2 mb-2">Khatian Type</div>
      <v-radio-group v-model="modelValue.collegeLandDetails.khatianType" row @update:model-value="updateValue">
        <v-radio v-for="option in khatianTypeOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <v-col cols="4">
      <v-text-field v-model="modelValue.collegeLandDetails.khatianNo" label="Khatian No" @input="updateValue" />
    </v-col>

    <v-col cols="6">
      <FileUploadField :label="'Khatian Documents'" :uploadedFiles="uploadedKhatianFiles" :rules="[]" @add="onAddKhatian" @remove="onRemoveKhatian" />
    </v-col>

    <v-col cols="2">
      <div class="text-body-2 mb-2">Plot Type</div>
      <v-radio-group v-model="modelValue.collegeLandDetails.plotType" row @update:model-value="updateValue">
        <v-radio v-for="option in plotTypeOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <v-col cols="4">
      <v-text-field v-model="modelValue.collegeLandDetails.plotNo" label="Plot No" @input="updateValue" />
    </v-col>

    <v-col cols="2">
      <div class="text-body-2 mb-2">Area Classification</div>
      <v-radio-group v-model="modelValue.collegeLandDetails.areaClassification" row @update:model-value="updateValue">
        <v-radio v-for="option in areaClassificationOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <!-- Area of land for the college -->
    <v-col cols="4">
      <v-text-field v-model="modelValue.collegeLandAreaInAcres" label="Area of land for the college (in acres)" type="number" step="0.01" :rules="[landAreaRule]" hint="'Minimum 3 acres (Urban) and 5 acres (Rural)'" @input="updateValue" />
    </v-col>

    <v-col cols="6">
      <FileUploadField :label="'College Land Documents'" :uploadedFiles="uploadedCollegeLandFiles" :rules="[]" @add="onAddCollegeLand" @remove="onRemoveCollegeLand" />
    </v-col>

    <!-- Area of covered/built-up space -->
    <v-col cols="6">
      <v-text-field v-model="modelValue.collegeCoveredArea" label="Area of covered/ built-up space (in sq feet)" type="number" step="0.01" :rules="[coveredAreaRule]" hint="Minimum 2000 sq ft for all classifications" @input="updateValue" />
    </v-col>

    <!-- Credibility and readiness of the applicant -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="12">
      <div class="text-subtitle-1"><strong>Credibility and readiness of the applicant</strong></div>
    </v-col>

    <v-col cols="4">
      <v-text-field v-model="modelValue.credibilityAndReadiness.experienceInEducation" label="Experience/Expertise in Education" @input="updateValue" />
    </v-col>

    <v-col cols="4">
      <v-text-field v-model="modelValue.credibilityAndReadiness.generalReputation" label="General Reputation" @input="updateValue" />
    </v-col>

    <v-col cols="">
      <v-text-field v-model="modelValue.credibilityAndReadiness.readinessToComplyWithRegulatoryNorms" label="Readiness to comply with regulatory norms" @input="updateValue" />
    </v-col>

    <!-- Additional commitments and plans -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="12">
      <div class="text-subtitle-1"><strong>Additional commitments and plans</strong></div>
    </v-col>

    <v-col cols="2">
      <div class="text-body-2 mb-2">Reservations for Students</div>
      <v-radio-group v-model="modelValue.additionalCommitmentsAndPlans.studentReservation" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>
    <v-col cols="4">
      <v-textarea v-model="modelValue.additionalCommitmentsAndPlans.studentReservationDetails" label="Reservations for Students (Details)" rows="3" auto-grow @input="updateValue" />
    </v-col>

    <v-col cols="6">
      <FileUploadField :label="'Student Reservation Documents'" :uploadedFiles="uploadedStudentReservationFiles" :rules="[]" @add="onAddStudentReservation" @remove="onRemoveStudentReservation" />
    </v-col>

    <v-col cols="3">
      <div class="text-body-2 mb-2">Reservations for Employees</div>
      <v-radio-group v-model="modelValue.additionalCommitmentsAndPlans.employeeReservation" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>
    <v-col cols="9">
      <v-textarea v-model="modelValue.additionalCommitmentsAndPlans.employeeReservationDetails" label="Reservations for Employees (Details)" rows="3" auto-grow @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <div class="text-body-2 mb-2">Special Skill Development Activities</div>
      <v-radio-group v-model="modelValue.additionalCommitmentsAndPlans.specialSkillDevelomentActivity" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>
    <v-col cols="9">
      <v-textarea v-model="modelValue.additionalCommitmentsAndPlans.specialSkillDetails" label="Special Skill Development Activities (Details)" rows="3" auto-grow @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <div class="text-body-2 mb-2">Academic Auditing Plans</div>
      <v-radio-group v-model="modelValue.additionalCommitmentsAndPlans.academicAuditingPlans" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>
    <v-col cols="9">
      <v-textarea v-model="modelValue.additionalCommitmentsAndPlans.academicAuditDetails" label="Academic Auditing Plans (Details)" rows="3" auto-grow @input="updateValue" />
    </v-col>

    <!-- Whether the Land has been owned/recorded in the name of the Institution (College/University) -->
    <v-col cols="3">
      <div class="text-body-2 mb-2">Whether the Land has been owned/recorded in the name of the Institution (College/University)</div>
      <v-radio-group v-model="modelValue.landStatus.landOwnedStatus" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <v-col cols="9">
      <v-textarea v-model="modelValue.comprehensivePlan" label="Comprehensive Plan" rows="3" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <FileUploadField :label="'Comprehensive Plan Files'" :uploadedFiles="uploadedComprehensivePlanFiles" :rules="[]" @add="onAddComprehensivePlan" @remove="onRemoveComprehensivePlan" />
    </v-col>

    <!-- Details of plan for campus development -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="12">
      <div class="text-subtitle-1">Details of plan for campus development such as construction of building, development of structural amenities and infrastructural facilities to be undertaken before the college starts functioning</div>
    </v-col>

    <!-- Building plan approved with -->
    <v-col cols="12">
      <div class="text-body-1 font-weight-medium mt-4 mb-2"><strong>Building plan approved with</strong></div>
    </v-col>

    <v-col cols="4">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.approvedPlanWith.totalBuildUpArea" label="Total build up area (in sq feet)" type="number" step="0.01" @input="updateValue" />
    </v-col>

    <v-col cols="4">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.approvedPlanWith.groundFloorArea" label="Ground floor area (in sq feet)" type="number" step="0.01" @input="updateValue" />
    </v-col>

    <v-col cols="4">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.approvedPlanWith.firstFloorArea" label="First floor area (in sq feet)" type="number" step="0.01" @input="updateValue" />
    </v-col>

    <!-- 10.2 Total Number of -->
    <v-col cols="12">
      <div class="text-body-1 font-weight-medium mt-4 mb-2"><strong>Total Number of</strong></div>
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.classRoomCount" label="Classroom" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.seminarRoomCount" label="Seminar/ Tutorial Room" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.multipurposeHallCount" label="Multipurpose Hall" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.labResourceCenterCount" label="Laboratories/ Resource Centres" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.ictEduTechLabCount" label="ICT / Educational Technology Lab" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.languageLabCount" label="Language Lab" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.storeRoomCount" label="Store Room" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.boysCommonRoomCount" label="Boys Common Room" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.girlsCommonRoomCount" label="Girls Common Room" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.boysToiletCount" label="Boys Toilet" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.girlsToiletCount" label="Girls Toilet" type="number" @input="updateValue" />
    </v-col>

    <!-- Any Other Room -->
    <v-col cols="12">
      <div class="text-body-1 font-weight-medium mt-4 mb-2"><strong>Any Other Room</strong></div>
    </v-col>

    <v-col cols="6">
      <div class="text-body-2 mb-2">Conference Room</div>
      <v-radio-group v-model="modelValue.campusDevlopmentPlan.anyOtherRoom.conferrenceRoomStatus" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <v-col cols="6">
      <div class="text-body-2 mb-2">Meeting Room</div>
      <v-radio-group v-model="modelValue.campusDevlopmentPlan.anyOtherRoom.meetingRoomStatus" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <!-- Library Details -->
    <v-col cols="12">
      <div class="text-body-1 font-weight-medium mt-4 mb-2"><strong>Library Details</strong></div>
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.libraryDetails.totalSpace" label="Total Space (in sq feet)" type="number" step="0.01" @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.libraryDetails.readingRoomCount" label="Total No of reading rooms" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.libraryDetails.booksCount" label="No of Books" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="3">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.libraryDetails.journalPeriodicalCount" label="No of Journal/Periodical etc" type="number" @input="updateValue" />
    </v-col>

    <!-- Administrative Office and Total Planned Construction -->
    <v-col cols="3">
      <div class="text-body-2 mb-2">Whether any Administrative Office</div>
      <v-radio-group v-model="modelValue.campusDevlopmentPlan.administrativeOfficeStatus" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <v-col cols="9">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalPlannedConstruction" label="Total Planned Construction (in Square Foot)" type="number" step="0.01" @input="updateValue" />
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { numericRule } from '@/composables/validators'
import FileUploadField from '@/components/ui/FileUploadField.vue'
import { useFileStore } from '@/stores/fileStore'

// Props
const props = defineProps<{
  modelValue: any
}>()

// Emits
const emit = defineEmits<{
  'update:modelValue': [value: any]
}>()

const fileStore = useFileStore()

const uploadedVisionFiles = ref<any[]>([])
const uploadedMissionFiles = ref<any[]>([])
const uploadedCoreValuesFiles = ref<any[]>([])
const uploadedAimsFiles = ref<any[]>([])
const uploadedObjectiveConcernedInstitutionFiles = ref<any[]>([])
const uploadedKhatianFiles = ref<any[]>([])
const uploadedCollegeLandFiles = ref<any[]>([])
const uploadedStudentReservationFiles = ref<any[]>([])
const uploadedComprehensivePlanFiles = ref<any[]>([])

function onAddVision(file: File | null) {
  return uploadFile(file, uploadedVisionFiles, 'Vision')
}
function onRemoveVision(index: number) {
  return removeItem(uploadedVisionFiles, index)
}

function onAddMission(file: File | null) {
  return uploadFile(file, uploadedMissionFiles, 'Mission')
}
function onRemoveMission(index: number) {
  return removeItem(uploadedMissionFiles, index)
}

function onAddCoreValues(file: File | null) {
  return uploadFile(file, uploadedCoreValuesFiles, 'Core Values')
}
function onRemoveCoreValues(index: number) {
  return removeItem(uploadedCoreValuesFiles, index)
}

function onAddAims(file: File | null) {
  return uploadFile(file, uploadedAimsFiles, 'Aims')
}
function onRemoveAims(index: number) {
  return removeItem(uploadedAimsFiles, index)
}

function onAddObjectiveConcernedInstitution(file: File | null) {
  return uploadFile(file, uploadedObjectiveConcernedInstitutionFiles, 'Objectives of Concerned Institution')
}
function onRemoveObjectiveConcernedInstitution(index: number) {
  return removeItem(uploadedObjectiveConcernedInstitutionFiles, index)
}

function onAddKhatian(file: File | null) {
  return uploadFile(file, uploadedKhatianFiles, 'Khatian Document')
}
function onRemoveKhatian(index: number) {
  return removeItem(uploadedKhatianFiles, index)
}

function onAddCollegeLand(file: File | null) {
  return uploadFile(file, uploadedCollegeLandFiles, 'College Land Document')
}
function onRemoveCollegeLand(index: number) {
  return removeItem(uploadedCollegeLandFiles, index)
}

function onAddStudentReservation(file: File | null) {
  return uploadFile(file, uploadedStudentReservationFiles, 'Student Reservation Document')
}
function onRemoveStudentReservation(index: number) {
  return removeItem(uploadedStudentReservationFiles, index)
}

function onAddComprehensivePlan(file: File | null) {
  return uploadFile(file, uploadedComprehensivePlanFiles, 'Comprehensive Plan')
}
function onRemoveComprehensivePlan(index: number) {
  return removeItem(uploadedComprehensivePlanFiles, index)
}

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

function removeItem(collection: any, index: number, options?: { minLength?: number }) {
  const minLength = options?.minLength ?? 0
  const arr = collection?.value ?? collection
  if (!Array.isArray(arr)) return
  if (index < 0 || index >= arr.length) return
  if (arr.length < minLength) return
  arr.splice(index, 1)
}

watch(uploadedVisionFiles, (newDocs: any[]) => {
  props.modelValue.aimAndObjective.visionFiles = newDocs.map((doc: any) => doc.id)
  updateValue()
}, { deep: true })

watch(uploadedMissionFiles, (newDocs: any[]) => {
  props.modelValue.aimAndObjective.missionFiles = newDocs.map((doc: any) => doc.id)
  updateValue()
}, { deep: true })

watch(uploadedCoreValuesFiles, (newDocs: any[]) => {
  props.modelValue.aimAndObjective.coreValuesFiles = newDocs.map((doc: any) => doc.id)
  updateValue()
}, { deep: true })

watch(uploadedAimsFiles, (newDocs: any[]) => {
  props.modelValue.aimAndObjective.aimsFiles = newDocs.map((doc: any) => doc.id)
  updateValue()
}, { deep: true })

watch(uploadedObjectiveConcernedInstitutionFiles, (newDocs: any[]) => {
  props.modelValue.aimAndObjective.objectiveConcernedInstitutionFiles = newDocs.map((doc: any) => doc.id)
  updateValue()
}, { deep: true })

watch(uploadedKhatianFiles, (newDocs: any[]) => {
  props.modelValue.collegeLandDetails.khatianFiles = newDocs.map((doc: any) => doc.id)
  updateValue()
}, { deep: true })

watch(uploadedCollegeLandFiles, (newDocs: any[]) => {
  props.modelValue.collegeLandFiles = newDocs.map((doc: any) => doc.id)
  updateValue()
}, { deep: true })

watch(uploadedStudentReservationFiles, (newDocs: any[]) => {
  props.modelValue.additionalCommitmentsAndPlans.studentReservationFiles = newDocs.map((doc: any) => doc.id)
  updateValue()
}, { deep: true })

watch(uploadedComprehensivePlanFiles, (newDocs: any[]) => {
  props.modelValue.comprehensivePlanFiles = newDocs.map((doc: any) => doc.id)
  updateValue()
}, { deep: true })

// Options for radio buttons
const yesNoOptions = [
  { label: 'Yes', value: 1 },
  { label: 'No', value: 0 }
]

// Land Area
const areaClassificationOptions = [
  { label: 'Urban', value: 1 },
  { label: 'Rural', value: 2 }
]

// Khatian Type
const khatianTypeOptions = [
  { label: 'LR', value: 1 },
  { label: 'RS', value: 2 }
]

// Plot Type
const plotTypeOptions = [
  { label: 'LR', value: 1 },
  { label: 'RS', value: 2 }
]

// Land area
function landAreaRule(value: any) {
  const classification = Number(props.modelValue?.collegeLandDetails?.areaClassification)
  if (!classification) return true

  const minRequired = classification === 2 ? 5 : 3
  const label = classification === 2 ? 'Rural' : 'Urban'
  const validator = numericRule({
    min: minRequired,
    allowDecimal: true,
    messages: {
      digits: 'Please enter a valid numeric value.',
      min: `Minimum ${minRequired} acres required for ${label} classification.`,
    },
  })

  return validator(value)
}

// Covered area
const coveredAreaRule = numericRule({
  min: 2000,
  allowDecimal: true,
  messages: {
    digits: 'Please enter a valid numeric value.',
    min: 'Minimum 2000 sq ft required.',
  },
})

function updateValue() {
  emit('update:modelValue', props.modelValue)
}
</script>

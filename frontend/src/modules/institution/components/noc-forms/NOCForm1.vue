<template>
  <v-row class="pa-2">
    <!-- Aims and objectives of the proposed self-financing UG college -->
    <v-col cols="12">
      <div class="text-subtitle-1">Aims and objectives of the proposed self-financing UG college</div>
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.aimAndObjective.vision" label="Vision" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.aimAndObjective.mission" label="Mission" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.aimAndObjective.coreValues" label="Core Values" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.aimAndObjective.aims" label="Aims" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.aimAndObjective.objectiveConcernedInstitution" label="Objectives of Concerned Institution" @input="updateValue" />
    </v-col>

    <!-- Details of the land of the college -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="12">
      <div class="text-subtitle-1">Details of the land of the college</div>
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.collegeLandDetails.mouza" label="Mouza" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.collegeLandDetails.jlNo" label="JL No" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <div class="text-body-2 mb-2">Khatian Type</div>
      <v-radio-group v-model="modelValue.collegeLandDetails.khatianType" row @update:model-value="updateValue">
        <v-radio v-for="option in khatianTypeOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.collegeLandDetails.khatianNo" label="Khatian No" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <div class="text-body-2 mb-2">Plot Type</div>
      <v-radio-group v-model="modelValue.collegeLandDetails.plotType" row @update:model-value="updateValue">
        <v-radio v-for="option in plotTypeOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.collegeLandDetails.plotNo" label="Plot No" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <div class="text-body-2 mb-2">Area Classification</div>
      <v-radio-group v-model="modelValue.collegeLandDetails.areaClasification" row @update:model-value="updateValue">
        <v-radio v-for="option in areaClassificationOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <!-- Area of land for the college -->
    <v-col cols="12">
      <v-text-field v-model="modelValue.collegeLandAreaInAcres" label="Area of land for the college (in acres)" type="number" step="0.01" :rules="[landAreaRule]" hint="'Minimum 3 acres (Urban) and 5 acres (Rural)'" @input="updateValue" />
    </v-col>

    <!-- Area of covered/built-up space -->
    <v-col cols="12">
      <v-text-field v-model="modelValue.collegeCoveredArea" label="Area of covered/ built-up space (in sq feet)" type="number" step="0.01" :rules="[coveredAreaRule]" hint="Minimum 2000 sq ft for all classifications" @input="updateValue" />
    </v-col>

    <!-- Credibility and readiness of the applicant -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="12">
      <div class="text-subtitle-1">Credibility and readiness of the applicant</div>
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.credibilityAndReadiness.experienceInEducation" label="Experience/Expertise in Education" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.credibilityAndReadiness.generalReputation" label="General Reputation" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.credibilityAndReadiness.readinessToComplyWithRegulatoryNorms" label="Readiness to comply with regulatory norms" @input="updateValue" />
    </v-col>

    <!-- Additional commitments and plans -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="12">
      <div class="text-subtitle-1">Additional commitments and plans</div>
    </v-col>

    <v-col cols="12">
      <div class="text-body-2 mb-2">Reservations for Students</div>
      <v-radio-group v-model="modelValue.additionalCommitmentsAndPlans.studentReservation" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>
    <v-col cols="12">
      <v-textarea v-model="modelValue.additionalCommitmentsAndPlans.studentReservationDetails" label="Reservations for Students (Details)" rows="3" auto-grow @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <div class="text-body-2 mb-2">Reservations for Employees</div>
      <v-radio-group v-model="modelValue.additionalCommitmentsAndPlans.employeeReservation" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>
    <v-col cols="12">
      <v-textarea v-model="modelValue.additionalCommitmentsAndPlans.employeeReservationDetails" label="Reservations for Employees (Details)" rows="3" auto-grow @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <div class="text-body-2 mb-2">Special Skill Development Activities</div>
      <v-radio-group v-model="modelValue.additionalCommitmentsAndPlans.specialSkillDevelomentActivity" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>
    <v-col cols="12">
      <v-textarea v-model="modelValue.additionalCommitmentsAndPlans.specialSkilDetails" label="Special Skill Development Activities (Details)" rows="3" auto-grow @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <div class="text-body-2 mb-2">Academic Auditing Plans</div>
      <v-radio-group v-model="modelValue.additionalCommitmentsAndPlans.academicAuditingPlans" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>
    <v-col cols="12">
      <v-textarea v-model="modelValue.additionalCommitmentsAndPlans.academicAuditDetails" label="Academic Auditing Plans (Details)" rows="3" auto-grow @input="updateValue" />
    </v-col>

    <!-- Whether the Land has been owned/recorded in the name of the Institution (College/University) -->
    <v-col cols="12">
      <div class="text-body-2 mb-2">Whether the Land has been owned/recorded in the name of the Institution (College/University)</div>
      <v-radio-group v-model="modelValue.landStatus.landOwnedStatus" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <!-- Insertion field will be replaced by Upload field -->
    <v-col cols="12">
      <v-textarea v-model="modelValue.comprehensivePlan" label="Insertion field will be replaced by Upload field" rows="3" @input="updateValue" />
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
      <div class="text-body-1 font-weight-medium mt-4 mb-2">Building plan approved with</div>
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.approvedPlanWith.totalBuildUpArea" label="Total build up area (in sq feet)" type="number" step="0.01" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.approvedPlanWith.groundFloorArea" label="Ground floor area (in sq feet)" type="number" step="0.01" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.approvedPlanWith.firstFloorArea" label="First floor area (in sq feet)" type="number" step="0.01" @input="updateValue" />
    </v-col>

    <!-- 10.2 Total Number of -->
    <v-col cols="12">
      <div class="text-body-1 font-weight-medium mt-4 mb-2">Total Number of</div>
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.classRoomCount" label="Classroom" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.seminarRoomCount" label="Seminar/ Tutorial Room" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.multipurposeHallCount" label="Multipurpose Hall" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.labResourceCenterCount" label="Laboratories/ Resource Centres" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.ictEduTechLabCount" label="ICT / Educational Technology Lab" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.languageLabCount" label="Language Lab" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.storeRoomCount" label="Store Room" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.boysCommonRoomCount" label="Boys Common Room" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.girlsCommonRoomCount" label="Girls Common Room" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.boysToiletCount" label="Boys Toilet" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalNumberOf.girlsToiletCount" label="Girls Toilet" type="number" @input="updateValue" />
    </v-col>

    <!-- Any Other Room -->
    <v-col cols="12">
      <div class="text-body-1 font-weight-medium mt-4 mb-2">Any Other Room</div>
    </v-col>

    <v-col cols="12">
      <div class="text-body-2 mb-2">Conference Room</div>
      <v-radio-group v-model="modelValue.campusDevlopmentPlan.anyOtherRoom.conferrenceRoomStatus" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <v-col cols="12">
      <div class="text-body-2 mb-2">Meeting Room</div>
      <v-radio-group v-model="modelValue.campusDevlopmentPlan.anyOtherRoom.meetingRoomStatus" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <!-- Library Details -->
    <v-col cols="12">
      <div class="text-body-1 font-weight-medium mt-4 mb-2">Library Details</div>
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.libraryDetails.totalSpace" label="Total Space (in sq feet)" type="number" step="0.01" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.libraryDetails.readingRoomCount" label="Total No of reading rooms" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.libraryDetails.booksCount" label="No of Books" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.libraryDetails.journalPeriodicalCount" label="No of Journal/Periodical etc" type="number" @input="updateValue" />
    </v-col>

    <!-- Administrative Office and Total Planned Construction -->
    <v-col cols="12">
      <div class="text-body-2 mb-2">Whether any Administrative Office</div>
      <v-radio-group v-model="modelValue.campusDevlopmentPlan.administrativeOfficeStatus" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <v-col cols="12">
      <v-text-field v-model="modelValue.campusDevlopmentPlan.totalPlannedConstruction" label="Total Planned Construction (in Square Foot)" type="number" step="0.01" @input="updateValue" />
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { numericRule } from '@/composables/validators'

// Props
const props = defineProps<{
  modelValue: any
}>()

// Emits
const emit = defineEmits<{
  'update:modelValue': [value: any]
}>()

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
  const classification = Number(props.modelValue?.collegeLandDetails?.areaClasification)
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

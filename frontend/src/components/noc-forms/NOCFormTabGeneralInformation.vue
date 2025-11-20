<template>
  <v-row class="pa-2">
    <!-- 1. Aims and objectives of the proposed self-financing UG college -->
    <v-col cols="12">
      <div class="text-subtitle-1">Aims and objectives of the proposed self-financing UG college</div>
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.aimAndObjective.vision"
        label="Vision"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.aimAndObjective.mission"
        label="Mission"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.aimAndObjective.coreValues"
        label="Core Values"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.aimAndObjective.aims"
        label="Aims"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.aimAndObjective.objectiveConcernedInstitution"
        label="Objectives of Concerned Institution"
        @input="updateValue"
      />
    </v-col>

    <!-- 2. Details of the land of the college -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="12">
      <div class="text-subtitle-1">Details of the land of the college</div>
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.collegeLandDetails.mouza"
        label="Mouza"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.collegeLandDetails.jlNo"
        label="JL No"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.collegeLandDetails.khatianNo"
        label="Khatian No"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.collegeLandDetails.plotNo"
        label="Plot No"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <div class="text-body-2 mb-2">Area Classification</div>
      <v-radio-group
        v-model="modelValue.collegeLandDetails.areaClasification"
        row
        @update:model-value="updateValue"
      >
        <v-radio
          v-for="option in areaClassificationOptions"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        />
      </v-radio-group>
    </v-col>

    <!-- 3. Area of land for the college -->
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.collegeLandAreaInAcres"
        label="Area of land for the college (in acres)"
        type="number"
        step="0.01"
        @input="updateValue"
      />
    </v-col>

    <!-- 4. Area of covered/built-up space -->
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.collegeCoveredArea"
        label="Area of covered/ built-up space (in sq meter)"
        type="number"
        step="0.01"
        @input="updateValue"
      />
    </v-col>

    <!-- 5. Credibility and readiness of the applicant -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="12">
      <div class="text-subtitle-1">Credibility and readiness of the applicant</div>
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.credibilityAndReadiness.experienceInEducation"
        label="Experience/Expertise in Education"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.credibilityAndReadiness.generalReputation"
        label="General Reputation"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.credibilityAndReadiness.readinessToComplyWithRegulatoryNorms"
        label="Readiness to comply with regulatory norms"
        @input="updateValue"
      />
    </v-col>

    <!-- 6. Additional commitments and plans -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="12">
      <div class="text-subtitle-1">Additional commitments and plans</div>
    </v-col>
    
    <v-col cols="12">
      <div class="text-body-2 mb-2">Reservations for Students</div>
      <v-radio-group
        v-model="modelValue.additionalCommitmentsAndPlans.studentReservation"
        row
        @update:model-value="updateValue"
      >
        <v-radio
          v-for="option in yesNoOptions"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        />
      </v-radio-group>
    </v-col>
    
    <v-col cols="12">
      <div class="text-body-2 mb-2">Reservations for Employees</div>
      <v-radio-group
        v-model="modelValue.additionalCommitmentsAndPlans.employeeReservation"
        row
        @update:model-value="updateValue"
      >
        <v-radio
          v-for="option in yesNoOptions"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        />
      </v-radio-group>
    </v-col>
    
    <v-col cols="12">
      <div class="text-body-2 mb-2">Special Skill Development Activities</div>
      <v-radio-group
        v-model="modelValue.additionalCommitmentsAndPlans.specialSkillDevelomentActivity"
        row
        @update:model-value="updateValue"
      >
        <v-radio
          v-for="option in yesNoOptions"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        />
      </v-radio-group>
    </v-col>
    
    <v-col cols="12">
      <div class="text-body-2 mb-2">Academic Auditing Plans</div>
      <v-radio-group
        v-model="modelValue.additionalCommitmentsAndPlans.academicAuditingPlans"
        row
        @update:model-value="updateValue"
      >
        <v-radio
          v-for="option in yesNoOptions"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        />
      </v-radio-group>
    </v-col>

    <!-- 7. Whether the land already owned -->
    <v-col cols="12">
      <div class="text-body-2 mb-2">Whether the land already owned</div>
      <v-radio-group
        v-model="modelValue.landOwnedStatus"
        row
        @update:model-value="updateValue"
      >
        <v-radio
          v-for="option in yesNoOptions"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        />
      </v-radio-group>
    </v-col>

    <!-- 8. Whether the land has been converted for educational purpose -->
    <v-col cols="12">
      <div class="text-body-2 mb-2">Whether the land has been converted for use of educational purpose or not</div>
      <v-radio-group
        v-model="modelValue.landConvertedForEducationalPurposeStatus"
        row
        @update:model-value="updateValue"
      >
        <v-radio
          v-for="option in yesNoOptions"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        />
      </v-radio-group>
    </v-col>

    <!-- 9. Comprehensive plan for the proposed college -->
    <v-col cols="12">
      <v-textarea
        v-model="modelValue.comprehensivePlan"
        label="Comprehensive plan for the proposed college"
        rows="3"
        @input="updateValue"
      />
    </v-col>

    <!-- 10. Details of plan for campus development -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="12">
      <div class="text-subtitle-1">Details of plan for campus development such as construction of building, development of structural amenities and infrastructural facilities to be undertaken before the college starts functioning</div>
    </v-col>

    <!-- 10.1 Building plan approved with -->
    <v-col cols="12">
      <div class="text-body-1 font-weight-medium mt-4 mb-2">Building plan approved with</div>
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.approvedPlanWith.totalBuildUpArea"
        label="Total build up area (in sq feet)"
        type="number"
        step="0.01"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.approvedPlanWith.groundFloorArea"
        label="Ground floor area (in sq feet)"
        type="number"
        step="0.01"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.approvedPlanWith.firstFloorArea"
        label="First floor area (in sq feet)"
        type="number"
        step="0.01"
        @input="updateValue"
      />
    </v-col>

    <!-- 10.2 Total Number of -->
    <v-col cols="12">
      <div class="text-body-1 font-weight-medium mt-4 mb-2">Total Number of</div>
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.totalNumberOf.classRoomCount"
        label="Classroom"
        type="number"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.totalNumberOf.seminarRoomCount"
        label="Seminar/ Tutorial Room"
        type="number"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.totalNumberOf.multipurposeHallCount"
        label="Multipurpose Hall"
        type="number"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.totalNumberOf.labResourceCenterCount"
        label="Laboratories/ Resource Centres"
        type="number"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.totalNumberOf.ictEduTechLabCount"
        label="ICT / Educational Technology Lab"
        type="number"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.totalNumberOf.languageLabCount"
        label="Language Lab"
        type="number"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.totalNumberOf.storeRoomCount"
        label="Store Room"
        type="number"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.totalNumberOf.boysCommonRoomCount"
        label="Boys Common Room"
        type="number"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.totalNumberOf.girlsCommonRoomCount"
        label="Girls Common Room"
        type="number"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.totalNumberOf.boysToiletCount"
        label="Boys Toilet"
        type="number"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.totalNumberOf.girlsToiletCount"
        label="Girls Toilet"
        type="number"
        @input="updateValue"
      />
    </v-col>

    <!-- 10.3 Any Other Room -->
    <v-col cols="12">
      <div class="text-body-1 font-weight-medium mt-4 mb-2">Any Other Room</div>
    </v-col>
    
    <v-col cols="12">
      <div class="text-body-2 mb-2">Conference Room</div>
      <v-radio-group
        v-model="modelValue.campusDevlopmentPlan.anyOtherRoom.conferrenceRoomStatus"
        row
        @update:model-value="updateValue"
      >
        <v-radio
          v-for="option in yesNoOptions"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        />
      </v-radio-group>
    </v-col>
    
    <v-col cols="12">
      <div class="text-body-2 mb-2">Meeting Room</div>
      <v-radio-group
        v-model="modelValue.campusDevlopmentPlan.anyOtherRoom.meetingRoomStatus"
        row
        @update:model-value="updateValue"
      >
        <v-radio
          v-for="option in yesNoOptions"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        />
      </v-radio-group>
    </v-col>

    <!-- 10.4 Library Details -->
    <v-col cols="12">
      <div class="text-body-1 font-weight-medium mt-4 mb-2">Library Details</div>
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.libraryDetails.totalSpace"
        label="Total Space (in sq feet)"
        type="number"
        step="0.01"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.libraryDetails.readingRoomCount"
        label="Total No of reading rooms"
        type="number"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.libraryDetails.booksCount"
        label="No of Books"
        type="number"
        @input="updateValue"
      />
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.libraryDetails.journalPeriodicalCount"
        label="No of Journal/Periodical etc"
        type="number"
        @input="updateValue"
      />
    </v-col>

    <!-- 10.5 Administrative Office and Total Planned Construction -->
    <v-col cols="12">
      <div class="text-body-2 mb-2">Whether any Administrative Office</div>
      <v-radio-group
        v-model="modelValue.campusDevlopmentPlan.administrativeOfficeStatus"
        row
        @update:model-value="updateValue"
      >
        <v-radio
          v-for="option in yesNoOptions"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        />
      </v-radio-group>
    </v-col>
    
    <v-col cols="12">
      <v-text-field
        v-model="modelValue.campusDevlopmentPlan.totalPlannedConstruction"
        label="Total Planned Construction (in Square Foot)"
        type="number"
        step="0.01"
        @input="updateValue"
      />
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
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

const areaClassificationOptions = [
  { label: 'Urban', value: 1 },
  { label: 'Rural', value: 2 }
]

function updateValue() {
  emit('update:modelValue', props.modelValue)
}
</script>

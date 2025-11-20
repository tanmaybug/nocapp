<template>
  <v-container>
    <v-card>
      <v-card-title class="text-center">Registration</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="onSubmit" ref="formRef">
          <v-row class="pa-2">
            <v-col cols="12">
              <v-autocomplete v-model.number="form.entityTypeID" :items="entityTypes" item-title="details" item-value="id" label="Category of Entity *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="form.applicantName" label="Name of the applicant(Society/ Trust/ Company/ Minority Institutions Eligible) *" :rules="[requiredRule]" />
            </v-col>

            <v-col cols="12">
              <div class="text-subtitle-1">Evidence of Registration</div>
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.isRegistered" :items="yesNoItems" item-title="label" item-value="value" label="Whether the society is registered under the Societies Registration Act? *" :rules="[requiredRule]" />
            </v-col>
            <template v-if="form.isRegistered === 1">
              <v-col cols="12">
                <v-text-field v-model="form.registrationNo" label="Registration No *" :rules="[requiredRule]" />
              </v-col>
              <v-col cols="12">
                <v-text-field v-model="form.registrationDate" type="date" label="Date of Registration *" :rules="[requiredRule]" />
              </v-col>
              <v-col cols="12">
                <v-text-field v-model="form.placeOfRegistration" label="Place of Registration *" :rules="[requiredRule]" />
              </v-col>
            </template>

            <v-col cols="12">
              <v-autocomplete v-model.number="form.minorityFlag" :items="yesNoItems" item-title="label" item-value="value" label="Is Minority? *" :rules="[requiredRule]" />
            </v-col>
            <template v-if="form.minorityFlag === 1">
              <v-col cols="12">
                <v-autocomplete v-model.number="form.minorityTypeId" :items="minorityTypes" item-title="details" item-value="id" label="Minority Type *" :rules="[requiredRule]" />
              </v-col>
              <v-col cols="12">
                <v-textarea v-model="form.minorityDetails" label="Details of Minority Status *" rows="3" :rules="[requiredRule]" />
              </v-col>
            </template>

            <v-col cols="12">
              <v-divider class="my-4"></v-divider>
            </v-col>

            <v-col cols="12">
              <div class="text-subtitle-1">Address of the Registered Office of the Applicant</div>
            </v-col>

            <v-col cols="12">
              <v-textarea v-model="form.applicantLocation.applicantAddress" label="Enter the Address Line of the applicant *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.applicantLocation.districtId" :items="districts" item-title="details" item-value="id" label="District *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.applicantLocation.subDivisionId" :items="applicantSubDivisions" item-title="details" item-value="id" label="Subdivision *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.applicantLocation.assemblyConstituencyId" :items="applicantAssemblyConstituencies" item-title="details" item-value="id" label="Assembly Constituency *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.applicantLocation.municipalityBlockId" :items="applicantMunicipalityBlocks" item-title="details" item-value="id" label="Municipality/Block *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="form.applicantLocation.city" label="City/Village *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.applicantLocation.policeStationId" :items="policeStations" item-title="details" item-value="id" label="Police Station *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-text-field v-model.number="form.applicantLocation.pin" label="PIN *" :rules="[requiredRule, pinRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.applicantLocation.postOfficeId" :items="applicantPostOffices" item-title="details" item-value="id" label="Post Office *" :rules="[requiredRule]" />
            </v-col>

            <v-col cols="12">
              <v-divider class="my-4"></v-divider>
            </v-col>

            <v-col cols="12">
              <v-text-field v-model="form.proposedCollegeName" label="Name of the proposed college *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.affiliatedUniversityId" :items="affiliatedUniversities" item-title="details" item-value="id" label="Name of the affiliated university *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.institutionForId" :items="instituteType" item-title="details" item-value="id" label="The institution is for *" :rules="[requiredRule]" />
            </v-col>

            <v-col cols="12">
              <v-divider class="my-4"></v-divider>
            </v-col>

            <v-col cols="12">
              <div class="text-subtitle-1">College Location</div>
            </v-col>

            <v-col cols="12">
              <v-textarea v-model="form.collegeLocation.collegeAddress" label="College Address *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.collegeLocation.districtId" :items="districts" item-title="details" item-value="id" label="District *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.collegeLocation.subDivisionId" :items="collegeSubDivisions" item-title="details" item-value="id" label="Subdivision *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.collegeLocation.assemblyConstituencyId" :items="collegeAssemblyConstituencies" item-title="details" item-value="id" label="Assembly Constituency *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.collegeLocation.municipalityBlockId" :items="collegeMunicipalityBlocks" item-title="details" item-value="id" label="Municipality/Block *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.collegeLocation.gramPanchayatId" :items="gramPanchayats" item-title="details" item-value="id" label="Gram Panchayat *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.collegeLocation.policeStationId" :items="policeStations" item-title="details" item-value="id" label="Police Station *" :rules="[requiredRule]" />
            </v-col>
            <v-col cols="12">
              <v-text-field v-model.number="form.collegeLocation.pin" label="PIN *" type="number" :rules="[requiredRule, pinRule]" />
            </v-col>
            <v-col cols="12">
              <v-autocomplete v-model.number="form.collegeLocation.postOfficeId" :items="collegePostOffices" item-title="details" item-value="id" label="Post Office *" :rules="[requiredRule]" />
            </v-col>

            <v-col cols="12">
              <v-divider class="my-4"></v-divider>
            </v-col>

            <v-col cols="12">
              <div class="text-subtitle-1">Applicant Contact Details</div>
            </v-col>

            <v-col cols="12">
              <v-text-field v-model.number="form.applicantMobileNo" label="Applicant Mobile Number *" :rules="[requiredRule, mobileRule]" type="tel" maxlength="10" />
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="form.applicantTanNo" label="Applicant TAN No" :rules="[alphanumericRule(10)]" maxlength="10" />
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="form.applicantEmailId" label="Applicant Email ID *" :rules="[requiredRule, emailRule]" type="email" />
            </v-col>

            <v-col cols="12">
              <v-divider class="my-4"></v-divider>
            </v-col>

            <v-col cols="12">
              <v-text-field v-model="form.password" label="Password *" :rules="[requiredRule, passwordRule]" :type="showPassword ? 'text' : 'password'" :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'" @click:append-inner="showPassword = !showPassword" autocomplete="new-password" />
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="confirmPassword" label="Confirm Password *" :rules="[requiredRule, confirmPasswordRule]" :type="showConfirmPassword ? 'text' : 'password'" :append-inner-icon="showConfirmPassword ? 'mdi-eye-off' : 'mdi-eye'" @click:append-inner="showConfirmPassword = !showConfirmPassword" autocomplete="new-password" />
            </v-col>
            <v-col cols="12" class="d-flex justify-end">
              <v-btn variant="text" @click="onReset">Reset</v-btn>
              <v-btn class="ms-2" :disabled="false" @click.prevent="onSubmit">Submit</v-btn>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { computed, onMounted, ref, watch, watchEffect } from 'vue'
import { requiredRule, passwordRule, makeMatchRule, numericRule, emailRule, alphanumericRule, mobileRule } from '@/composables/validators'
import type { SubDivision } from '@/types/common'
import { useRegistrationStore } from '@/stores/registrationStore'
import { storeToRefs } from 'pinia'

const store = useRegistrationStore()

const {
  form,
  entityTypes,
  minorityTypes,
  districts,
  subDivisions,
  policeStations,
  applicantPostOffices,
  collegePostOffices,
  assemblyConstituencies,
  municipalityBlocks,
  gramPanchayats,
  instituteType,
  affiliatedUniversities
} = storeToRefs(store)
const yesNoItems = [
  { label: 'Yes', value: 1 },
  { label: 'No', value: 0 },
]
const formRef = ref<any>(null)

// Entity Type
watchEffect(() => {
  if (form.value.entityTypeID === 4) {
    form.value.minorityFlag = 1
  }
})

// District
watch(() => form.value.applicantLocation.districtId, (n, o) => {
  if (n !== o) {
    form.value.applicantLocation.subDivisionId = null
    form.value.applicantLocation.assemblyConstituencyId = null
  }
})
watch(() => form.value.collegeLocation.districtId, (n, o) => {
  if (n !== o) {
    form.value.collegeLocation.subDivisionId = null
    form.value.collegeLocation.assemblyConstituencyId = null
  }
})

// Subdivision
const applicantSubDivisions = computed<SubDivision[]>(() => {
  const selectedDistrictId = form.value.applicantLocation.districtId
  if (!selectedDistrictId) return []
  return (subDivisions.value || []).filter((s: any) => s.districtId === selectedDistrictId)
})
const collegeSubDivisions = computed<SubDivision[]>(() => {
  const selectedDistrictId = form.value.collegeLocation.districtId
  if (!selectedDistrictId) return []
  return (subDivisions.value || []).filter((s: any) => s.districtId === selectedDistrictId)
})
watch(() => form.value.applicantLocation.subDivisionId, (n, o) => {
  if (n !== o) {
    form.value.applicantLocation.municipalityBlockId = null
  }
})
watch(() => form.value.collegeLocation.subDivisionId, (n, o) => {
  if (n !== o) {
    form.value.collegeLocation.municipalityBlockId = null
  }
})

// Assembly Constituency
const applicantAssemblyConstituencies = computed<any[]>(() => {
  const selectedDistrictId = form.value.applicantLocation.districtId
  if (!selectedDistrictId) return []
  return (assemblyConstituencies.value || []).filter((s: any) => s.districtId === selectedDistrictId)
})
const collegeAssemblyConstituencies = computed<any[]>(() => {
  const selectedDistrictId = form.value.collegeLocation.districtId
  if (!selectedDistrictId) return []
  return (assemblyConstituencies.value || []).filter((s: any) => s.districtId === selectedDistrictId)
})

// Municipality/Block
const applicantMunicipalityBlocks = computed<any[]>(() => {
  const selectedSubDivisionId = form.value.applicantLocation.subDivisionId
  if (!selectedSubDivisionId) return []
  return (municipalityBlocks.value || []).filter((s: any) => s.subDivId === selectedSubDivisionId)
})
const collegeMunicipalityBlocks = computed<any[]>(() => {
  const selectedSubDivisionId = form.value.collegeLocation.subDivisionId
  if (!selectedSubDivisionId) return []
  return (municipalityBlocks.value || []).filter((s: any) => s.subDivId === selectedSubDivisionId)
})
watchEffect(() => {
  const municipalityBlockId = form.value.collegeLocation.municipalityBlockId
  if (municipalityBlockId) {
    store.getGramPanchayats(municipalityBlockId)
  } else {
    gramPanchayats.value = []
    form.value.collegeLocation.gramPanchayatId = null
  }
})

// Pin
const pinRule = numericRule({ length: 6 })
watchEffect(() => {
  const pin = form.value.applicantLocation.pin
  if (pin && pin.toString().length === 6) {
    store.getPostOffices('applicant', pin)
  } else {
    applicantPostOffices.value = []
    form.value.applicantLocation.postOfficeId = null
  }
})
watchEffect(() => {
  const pin = form.value.collegeLocation.pin
  if (pin && pin.toString().length === 6) {
    store.getPostOffices('college', pin)
  } else {
    collegePostOffices.value = []
    form.value.collegeLocation.postOfficeId = null
  }
})

// Confirm Password
const confirmPasswordRule = makeMatchRule(() => form.value.password, 'Passwords do not match')

async function onSubmit() {
  const validation = await formRef.value.validate()
  if (!validation.valid) return

  await store.submitRegistration()
}
function onReset() {
  store.resetForm()
}

onMounted(async () => {
  onReset()
  await store.getFormOptions()
})

// Password
const confirmPassword = ref('')
const showPassword = ref(false)
const showConfirmPassword = ref(false)
</script>

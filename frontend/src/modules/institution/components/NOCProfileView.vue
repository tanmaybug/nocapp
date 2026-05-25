<template>
  <v-container class="py-6">
    <v-row justify="center">
      <v-col cols="12" lg="10" xl="9">
        <v-card elevation="2" :loading="status === 'processing'">
          <v-card-title>
            <div class="text-h5 text-primary font-weight-medium">NOC Application</div>
            <div class="text-subtitle-1 text-medium-emphasis">Application Details</div>
          </v-card-title>
          <v-divider />

          <v-card-text>
            <v-card variant="tonal" class="mb-4">
              <v-card-title class="text-subtitle-1 font-weight-medium">Applicant Details</v-card-title>
              <v-divider />
              <v-card-text>
                <v-table density="compact">
                  <tbody>
                    <tr>
                      <th class="label">Registration ID</th>
                      <td>{{ applicantDetails?.applicationId }}</td>
                      <th class="label">Applicant Name</th>
                      <td>{{ applicantDetails?.applicantName }}</td>
                    </tr>
                    <tr>
                      <th class="label">Mobile No.</th>
                      <td>{{ applicantDetails?.applicantMobileNo }}</td>
                      <th class="label">Email ID</th>
                      <td>{{ applicantDetails?.applicantEmailId }}</td>
                    </tr>
                    <tr>
                      <th class="label">Entity Type</th>
                      <td>{{ applicantDetails?.entityType }}</td>
                      <th class="label">Is Minority?</th>
                      <td>{{ applicantDetails?.isMinority }}</td>
                    </tr>
                    <tr>
                      <th class="label">Minority Type</th>
                      <td>{{ applicantDetails?.minorityType }}</td>
                      <th class="label">Minority Details</th>
                      <td>{{ applicantDetails?.language || applicantDetails?.religion }}</td>
                    </tr>
                    <tr>
                      <th class="label">Applicant TAN No</th>
                      <td>{{ applicantDetails?.applicantTanNo }}</td>
                      <th class="label"></th>
                      <td></td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Address Details</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Address</th>
                      <td>{{ applicantDetails?.applicantLocation?.applicantAddress }}</td>
                      <th class="label">District</th>
                      <td>{{ applicantDetails?.applicantLocation?.district }}</td>
                    </tr>
                    <tr>
                      <th class="label">Sub Division</th>
                      <td>{{ applicantDetails?.applicantLocation?.subDivision }}</td>
                      <th class="label">Police Station</th>
                      <td>{{ applicantDetails?.applicantLocation?.policeStation }}</td>
                    </tr>
                    <tr>
                      <th class="label">Post Office</th>
                      <td>{{ applicantDetails?.applicantLocation?.postOffice }}</td>
                      <th class="label">Municipality Block</th>
                      <td>{{ applicantDetails?.applicantLocation?.municipalityBlock }}</td>
                    </tr>
                    <tr>
                      <th class="label">City</th>
                      <td>{{ applicantDetails?.applicantLocation?.city }}</td>
                      <th class="label">PIN</th>
                      <td>{{ applicantDetails?.applicantLocation?.pin }}</td>
                    </tr>
                  </tbody>
                </v-table>
              </v-card-text>
            </v-card>

            <v-card variant="tonal" class="mb-4">
              <v-card-title class="text-subtitle-1 font-weight-medium">Institution Details</v-card-title>
              <v-divider />
              <v-card-text>
                <v-table density="compact">
                  <tbody>
                    <tr>
                      <th class="label">Proposed College Name</th>
                      <td>{{ collegeDetails?.proposedCollegeName }}</td>
                      <th class="label">Affiliated University</th>
                      <td>{{ collegeDetails?.affiliatedUniversity }}</td>
                    </tr>
                    <tr>
                      <th class="label">Institution For</th>
                      <td>{{ collegeDetails?.institutionFor }}</td>
                      <th class="label"></th>
                      <td></td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Address Details</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Address</th>
                      <td>{{ collegeDetails?.collegeLocation?.collegeAddress }}</td>
                      <th class="label">District</th>
                      <td>{{ collegeDetails?.collegeLocation?.districtId }}</td>
                    </tr>
                    <tr>
                      <th class="label">Sub Division</th>
                      <td>{{ collegeDetails?.collegeLocation?.subDivisionId }}</td>
                      <th class="label">Police Station</th>
                      <td>{{ collegeDetails?.collegeLocation?.policeStation }}</td>
                    </tr>
                    <tr>
                      <th class="label">Post Office</th>
                      <td>{{ collegeDetails?.collegeLocation?.postOffice }}</td>
                      <th class="label">Municipality Block</th>
                      <td>{{ collegeDetails?.collegeLocation?.municipalityBlock }}</td>
                    </tr>
                    <tr>
                      <th class="label">Gram Panchayat</th>
                      <td>{{ collegeDetails?.collegeLocation?.gramPanchayat }}</td>
                      <th class="label">PIN</th>
                      <td>{{ collegeDetails?.collegeLocation?.pin }}</td>
                    </tr>
                  </tbody>
                </v-table>
              </v-card-text>
            </v-card>

            <v-card variant="tonal" class="mb-4">
              <v-card-title class="text-subtitle-1 font-weight-medium">Institution Purpose</v-card-title>
              <v-divider />
              <v-card-text>
                <v-table density="compact">
                  <tbody>
                    <tr>
                      <th class="label">Vision</th>
                      <td colspan="3">{{ institutionPurpose?.aimAndObjective?.vision }}</td>
                    </tr>
                    <tr>
                      <th class="label">Mission</th>
                      <td colspan="3">{{ institutionPurpose?.aimAndObjective?.mission }}</td>
                    </tr>
                    <tr>
                      <th class="label">Core Values</th>
                      <td colspan="3">{{ institutionPurpose?.aimAndObjective?.coreValues }}</td>
                    </tr>
                    <tr>
                      <th class="label">Aims</th>
                      <td colspan="3">{{ institutionPurpose?.aimAndObjective?.aims }}</td>
                    </tr>
                    <tr>
                      <th class="label">Objective Concerned Institution</th>
                      <td colspan="3">{{ institutionPurpose?.aimAndObjective?.objectiveConcernedInstitution }}</td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Institution Land Details</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Mouza</th>
                      <td>{{ institutionPurpose?.collegeLandDetails?.mouza }}</td>
                      <th class="label">JlNo</th>
                      <td>{{ institutionPurpose?.collegeLandDetails?.jlNo }}</td>
                    </tr>
                    <tr>
                      <th class="label">KhatianNo</th>
                      <td>{{ institutionPurpose?.collegeLandDetails?.khatianNo }}</td>
                      <th class="label">Plot No</th>
                      <td>{{ institutionPurpose?.collegeLandDetails?.plotNo }}</td>
                    </tr>
                    <tr>
                      <th class="label">Area Clasification</th>
                      <td>{{ institutionPurpose?.collegeLandDetails?.areaClasification }}</td>
                      <th class="label"></th>
                      <td></td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Credibility And Readiness</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Experience In Education</th>
                      <td colspan="3">{{ institutionPurpose?.credibilityAndReadiness?.experienceInEducation }}</td>
                    </tr>
                    <tr>
                      <th class="label">General Reputation</th>
                      <td colspan="3">{{ institutionPurpose?.credibilityAndReadiness?.generalReputation }}</td>
                    </tr>
                    <tr>
                      <th class="label">Readiness To Comply With Regulatory Norms</th>
                      <td colspan="3">{{ institutionPurpose?.credibilityAndReadiness?.readinessToComplyWithRegulatoryNorms }}</td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Additional Commitments And Plans</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Student Reservation</th>
                      <td>{{ yesNo(institutionPurpose?.additionalCommitmentsAndPlans?.studentReservation) }}</td>
                      <th class="label">Employee Reservation</th>
                      <td>{{ yesNo(institutionPurpose?.additionalCommitmentsAndPlans?.employeeReservation) }}</td>
                    </tr>
                    <tr>
                      <th class="label">Special Skill Development Activity</th>
                      <td>{{ yesNo(institutionPurpose?.additionalCommitmentsAndPlans?.specialSkillDevelopmentActivity) }}</td>
                      <th class="label">Academic Auditing Plans</th>
                      <td>{{ yesNo(institutionPurpose?.additionalCommitmentsAndPlans?.academicAuditingPlans) }}</td>
                    </tr>
                  </tbody>
                </v-table>
              </v-card-text>
            </v-card>

            <v-card variant="tonal" class="mb-4">
              <v-card-title class="text-subtitle-1 font-weight-medium">Campus Development Details</v-card-title>
              <v-divider />
              <v-card-text>
                <v-table density="compact">
                  <tbody>
                    <tr>
                      <th class="label">Total Built-Up Area</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.approvedPlanWith?.totalBuildUpArea }}</td>
                      <th class="label">Ground Floor Area</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.approvedPlanWith?.groundFloorArea }}</td>
                    </tr>
                    <tr>
                      <th class="label">First Floor Area</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.approvedPlanWith?.firstFloorArea }}</td>
                      <th class="label"></th>
                      <td></td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Total Number Of</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Class Room Count</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.totalNumberOf?.classRoomCount }}</td>
                      <th class="label">Seminar Room Count</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.totalNumberOf?.seminarRoomCount }}</td>
                    </tr>
                    <tr>
                      <th class="label">Multipurpose Hall Count</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.totalNumberOf?.multipurposeHallCount }}</td>
                      <th class="label">Lab Resource Center Count</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.totalNumberOf?.labResourceCenterCount }}</td>
                    </tr>
                    <tr>
                      <th class="label">ICT EduTech Lab Count</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.totalNumberOf?.ictEduTechLabCount }}</td>
                      <th class="label">Language Lab Count</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.totalNumberOf?.languageLabCount }}</td>
                    </tr>
                    <tr>
                      <th class="label">Store Room Count</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.totalNumberOf?.storeRoomCount }}</td>
                      <th class="label">Boys CommonRoom Count</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.totalNumberOf?.boysCommonRoomCount }}</td>
                    </tr>
                    <tr>
                      <th class="label">Girls Common Room Count</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.totalNumberOf?.girlsCommonRoomCount }}</td>
                      <th class="label">Boys Toilet Count</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.totalNumberOf?.boysToiletCount }}</td>
                    </tr>
                    <tr>
                      <th class="label">Girls Toilet Count</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.totalNumberOf?.girlsToiletCount }}</td>
                      <th class="label"></th>
                      <td></td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Any Other Room</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Conferrence Room Status</th>
                      <td>{{ yesNo(campusDevelopment?.campusDevlopmentPlan?.anyOtherRoom?.conferrenceRoomStatus) }}</td>
                      <th class="label">Meeting Room Status</th>
                      <td>{{ yesNo(campusDevelopment?.campusDevlopmentPlan?.anyOtherRoom?.meetingRoomStatus) }}</td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Library Details</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Total Space</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.libraryDetails?.totalSpace }}</td>
                      <th class="label">Reading Room Count</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.libraryDetails?.readingRoomCount }}</td>
                    </tr>
                    <tr>
                      <th class="label">Books Count</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.libraryDetails?.booksCount }}</td>
                      <th class="label">Journal Periodical Count</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.libraryDetails?.journalPeriodicalCount }}</td>
                    </tr>
                    <tr>
                      <th class="label">Administrative Office Status</th>
                      <td>{{ yesNo(campusDevelopment?.campusDevlopmentPlan?.administrativeOfficeStatus) }}</td>
                      <th class="label">Total Planned Construction</th>
                      <td>{{ campusDevelopment?.campusDevlopmentPlan?.totalPlannedConstruction }}</td>
                    </tr>
                    <tr>
                      <th class="label">College Covered Area</th>
                      <td>{{ campusDevelopment?.collegeCoveredArea }}</td>
                      <th class="label">College Land Area In Acres</th>
                      <td>{{ campusDevelopment?.collegeLandAreaInAcres }}</td>
                    </tr>
                    <tr>
                      <th class="label">Comprehensive Plan</th>
                      <td colspan="3">{{ campusDevelopment?.comprehensivePlan }}</td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Land Status</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Land Owned Status</th>
                      <td>{{ yesNo(campusDevelopment?.landStatus?.landOwnedStatus) }}</td>
                      <th class="label">Land Converted For Educational Purpose Status</th>
                      <td>{{ yesNo(campusDevelopment?.landStatus?.landConvertedForEducationalPurposeStatus) }}</td>
                    </tr>
                  </tbody>
                </v-table>
              </v-card-text>
            </v-card>

            <v-card variant="tonal" class="mb-4">
              <v-card-title class="text-subtitle-1 font-weight-medium">Financial Details</v-card-title>
              <v-divider />
              <v-card-text>
                <v-table density="compact">
                  <tbody>
                    <tr>
                      <th class="label">Amount</th>
                      <td>{{ financialDetails?.projectedFundFlow?.amount }}</td>
                      <th class="label">Source Of Fund</th>
                      <td>{{ financialDetails?.projectedFundFlow?.sourceOfFund }}</td>
                    </tr>
                    <tr>
                      <th class="label">Building Completion Status</th>
                      <td>{{ financialDetails?.buildingCompletionStatus }}</td>
                      <th class="label">Building Completion Date</th>
                      <td>{{ financialDetails?.buildingCompletionDate }}</td>
                    </tr>
                    <tr>
                      <th class="label">Building Completion Expected Date</th>
                      <td>{{ financialDetails?.buildingCompletionExpectedDate }}</td>
                      <th class="label">Building Plan Amount To Be Deposited</th>
                      <td>{{ financialDetails?.buildingPlanAmountToBeDeposited }}</td>
                    </tr>
                    <tr>
                      <th class="label">Nationalized Bank</th>
                      <td>{{ financialDetails?.nationalizedBank }}</td>
                      <th class="label"></th>
                      <td></td>
                    </tr>
                    <tr>
                      <th class="label">Estimated Income And Expenditure For First 5 Years</th>
                      <td colspan="3">{{ financialDetails?.estimatedIncomeAndExpenditureForFirst5Years }}</td>
                    </tr>
                    <tr>
                      <th class="label">Initial Fund Information</th>
                      <td colspan="3">{{ financialDetails?.initialFundInformation }}</td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Synopsis</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Proposed Investment</th>
                      <td>{{ financialDetails?.synopsis?.proposedInvestment }}</td>
                      <th class="label">Proposed Employment</th>
                      <td>{{ financialDetails?.synopsis?.proposedEmployment }}</td>
                    </tr>
                    <tr>
                      <th class="label">Professional Colleges Count Within 25 Km</th>
                      <td>{{ financialDetails?.synopsis?.professionalCollegesCountWithin25Km }}</td>
                      <th class="label">Feeder School Count With in 15 Km</th>
                      <td>{{ financialDetails?.synopsis?.feederSchoolCountWithin15Km }}</td>
                    </tr>
                  </tbody>
                </v-table>
              </v-card-text>
            </v-card>

            <v-card variant="tonal">
              <v-card-title class="text-subtitle-1 font-weight-medium">Upload Documents</v-card-title>
              <v-divider />
              <v-card-text>
                <v-table density="compact">
                  <tbody>
                    <tr v-for="doc in documents" :key="doc.fieldName" class="doc-row">
                      <td colspan="4" class="doc-cell">
                        <div class="d-flex align-center justify-space-between ga-4">
                          <span>{{ doc.label }}</span>
                          <v-icon v-if="doc.filePath" icon="mdi-check-circle" color="success" />
                          <v-icon v-else icon="mdi-close-circle" color="error" />
                        </div>
                      </td>
                    </tr>
                    <tr v-if="!documents.length">
                      <td colspan="4" class="text-center text-grey-darken-1 py-4">No documents uploaded.</td>
                    </tr>
                  </tbody>
                </v-table>
              </v-card-text>
            </v-card>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import { useInstitutionStore } from '../stores'

const institutionStore = useInstitutionStore()
const { nocApplicationView, status } = storeToRefs(institutionStore)

const applicantDetails = computed(() => nocApplicationView.value?.applicantDetails)
const collegeDetails = computed(() => nocApplicationView.value?.collegeDetails)
const institutionPurpose = computed(() => nocApplicationView.value?.institutionPurpose)
const campusDevelopment = computed(() => nocApplicationView.value?.campusDevelopment)
const financialDetails = computed(() => nocApplicationView.value?.financialDetails)

const yesNo = (v?: number | null) => (v === 1 ? 'YES' : v === 0 ? 'NO' : '')

const documents = computed(() => nocApplicationView.value?.documentData ?? [])

onMounted(() => {
  institutionStore.getNOCApplicationView()
})
</script>

<style scoped>
:deep(.v-table table) {
  table-layout: fixed;
  width: 100%;
}

:deep(.v-table tbody > tr > th),
:deep(.v-table tbody > tr > td) {
  width: 25%;
  vertical-align: top;
  word-break: break-word;
}

.label {
  font-weight: 600;
}
</style>

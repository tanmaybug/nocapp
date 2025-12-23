<template>
  <v-container class="py-6">
    <v-row justify="center">
      <v-col cols="12" lg="10" xl="9">
        <v-card elevation="2">
          <v-card-title>
            <div>
              <div class="text-h5 text-primary fw-600">NOC Application</div>
              <div class="text-subtitle-1 text-medium-emphasis">Application Details</div>
            </div>
          </v-card-title>
          <v-divider />

          <v-card-text>
            <v-card variant="tonal" class="mb-4">
              <v-card-title class="text-subtitle-1 fw-600">Applicant Details</v-card-title>
              <v-divider />
              <v-card-text>
                <v-table density="compact">
                  <tbody>
                    <tr>
                      <th class="label">Registration ID</th>
                      <td>{{ applicantDetails.registrationNo }}</td>
                      <th class="label">Applicant Name</th>
                      <td>{{ applicantDetails.applicantName }}</td>
                    </tr>
                    <tr>
                      <th class="label">Mobile No.</th>
                      <td>{{ applicantDetails.applicantMobileNo }}</td>
                      <th class="label">Email ID</th>
                      <td>{{ applicantDetails.applicantEmailId }}</td>
                    </tr>
                    <tr>
                      <th class="label">Entity Type</th>
                      <td>{{ applicantDetails.entityType }}</td>
                      <th class="label">Is Registered?</th>
                      <td>{{ applicantDetails.isRegistered }}</td>
                    </tr>
                  </tbody>
                </v-table>
              </v-card-text>
            </v-card>

            <v-card variant="tonal" class="mb-4">
              <v-card-title class="text-subtitle-1 fw-600">Institution Details</v-card-title>
              <v-divider />
              <v-card-text>
                <v-table density="compact">
                  <tbody>
                    <tr>
                      <th class="label">Proposed College Name</th>
                      <td>{{ collegeDetails.proposedCollegeName }}</td>
                      <th class="label">Affiliated University</th>
                      <td>{{ collegeDetails.affiliatedUniversity }}</td>
                    </tr>
                    <tr>
                      <th class="label">Institution For</th>
                      <td>{{ collegeDetails.institutionFor }}</td>
                      <th class="label"></th>
                      <td></td>
                    </tr>
                  </tbody>
                </v-table>
              </v-card-text>
            </v-card>

            <v-card variant="tonal" class="mb-4">
              <v-card-title class="text-subtitle-1 fw-600">Institution Purpose</v-card-title>
              <v-divider />
              <v-card-text>
                <v-table density="compact">
                  <tbody>
                    <tr>
                      <th class="label">Vision</th>
                      <td>{{ institutionPurpose.aimAndObjective.vision }}</td>
                      <th class="label">Mission</th>
                      <td>{{ institutionPurpose.aimAndObjective.mission }}</td>
                    </tr>
                    <tr>
                      <th class="label">Core Values</th>
                      <td>{{ institutionPurpose.aimAndObjective.coreValues }}</td>
                      <th class="label">Aims</th>
                      <td>{{ institutionPurpose.aimAndObjective.aims }}</td>
                    </tr>
                  </tbody>
                </v-table>
              </v-card-text>
            </v-card>

            <v-card variant="tonal" class="mb-4">
              <v-card-title class="text-subtitle-1 fw-600">Campus Development Details</v-card-title>
              <v-divider />
              <v-card-text>
                <v-table density="compact">
                  <tbody>
                    <tr>
                      <th class="label">Total Built-Up Area</th>
                      <td>{{ campusDevelopment.campusDevlopmentPlan.approvedPlanWith.totalBuildUpArea }}</td>
                      <th class="label">Ground Floor Area</th>
                      <td>{{ campusDevelopment.campusDevlopmentPlan.approvedPlanWith.groundFloorArea }}</td>
                    </tr>
                    <tr>
                      <th class="label">First Floor Area</th>
                      <td>{{ campusDevelopment.campusDevlopmentPlan.approvedPlanWith.firstFloorArea }}</td>
                      <th class="label"></th>
                      <td></td>
                    </tr>
                  </tbody>
                </v-table>
              </v-card-text>
            </v-card>

            <v-card variant="tonal">
              <v-card-title class="text-subtitle-1 fw-600">Upload Documents</v-card-title>
              <v-divider />
              <v-card-text>
                <v-table density="compact">
                  <tbody>
                    <tr>
                      <th class="label">Proposal For Campus Development Program</th>
                      <td>
                        <v-icon icon="mdi-check-circle" color="success" />
                      </td>
                      <th class="label">Experience And Expertise In Discipline</th>
                      <td>
                        <v-icon icon="mdi-check-circle" color="success" />
                      </td>
                    </tr>
                  </tbody>
                </v-table>
              </v-card-text>
            </v-card>

            <v-alert variant="tonal" color="warning" class="mt-4">
              <div class="fw-600 mb-1">Self Declaration</div>
              <div class="text-body-2">
                I Shri/ Smt {{ applicantDetails.applicantName }} do hereby declare that I / my parents/ legal guardian/ my family have/ has been residing in the State of West Bengal since last 10 years (or more). I further declare that the above-mentioned information furnished by me is correct and true to my knowledge and belief.
              </div>
            </v-alert>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
const applicantDetails = {
  registrationNo: '12345',
  applicantName: 'Tanmay',
  applicantMobileNo: '9876543210',
  applicantEmailId: 'tanmay@example.com',
  entityType: 'Private',
  isRegistered: 'YES',
}

const collegeDetails = {
  proposedCollegeName: 'XYZ Engineering College',
  affiliatedUniversity: 'XYZ University',
  institutionFor: 'Engineering',
}

const institutionPurpose = {
  aimAndObjective: {
    vision: 'To be a premier institution promoting innovation and excellence in engineering education.',
    mission: 'To provide world-class education, foster innovation, and create socially responsible engineers.',
    coreValues: 'Integrity, Excellence, Innovation, Inclusivity, Sustainability',
    aims: 'To provide a platform for young minds to achieve academic and personal growth, contributing to societal welfare.',
  },
}

const campusDevelopment = {
  campusDevlopmentPlan: {
    approvedPlanWith: {
      totalBuildUpArea: '30000',
      groundFloorArea: '10000',
      firstFloorArea: '9000',
    },
  },
}
</script>

<style scoped>
.fw-600 {
  font-weight: 600;
}

.label {
  width: 22%;
  font-weight: 600;
  white-space: nowrap;
}
</style>

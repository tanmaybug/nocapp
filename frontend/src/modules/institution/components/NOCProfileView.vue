<template>
  <v-container class="py-6">
    <v-row justify="center">
      <v-col cols="12" lg="10" xl="9">
        <v-card elevation="2">
          <v-card-title>
            <div class="d-flex align-center justify-space-between flex-wrap ga-4">
              <div>
                <div class="text-h5 text-primary font-weight-medium">NOC Application</div>
                <div class="text-subtitle-1 text-medium-emphasis">Application Details</div>
              </div>
              <v-btn color="primary" variant="outlined" @click="docketDialog = true">Add docket Number</v-btn>
            </div>
          </v-card-title>
          <v-divider />

          <v-dialog v-model="docketDialog" max-width="420">
            <v-card>
              <v-card-title class="text-subtitle-1 font-weight-medium">Add docket Number</v-card-title>
              <v-divider />
              <v-card-text>
                <v-text-field v-model="docketNumber" label="Docket number" density="compact" variant="outlined" hide-details />
              </v-card-text>
              <v-divider />
              <v-card-actions>
                <v-spacer />
                <v-btn variant="text" @click="docketDialog = false">Close</v-btn>
                <v-btn color="primary" @click="saveDocketNumber">Save</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>

          <v-card-text>
            <v-card variant="tonal" class="mb-4">
              <v-card-title class="text-subtitle-1 font-weight-medium">Applicant Details</v-card-title>
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
                    <tr>
                      <th class="label">Minority Type</th>
                      <td></td>
                      <th class="label">Registration No</th>
                      <td>123456</td>
                    </tr>
                    <tr>
                      <th class="label">Registration Date</th>
                      <td>12-10-2025</td>
                      <th class="label">Place Of Registration</th>
                      <td>Howrah</td>
                    </tr>
                    <tr>
                      <th class="label">Minority Details</th>
                      <td></td>
                      <th class="label">Applicant TAN No</th>
                      <td>1234567890</td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Address Details</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Address</th>
                      <td>XYZ Test Address</td>
                      <th class="label">District</th>
                      <td>Howrah</td>
                    </tr>
                    <tr>
                      <th class="label">Sub Division</th>
                      <td>Howrah Sub</td>
                      <th class="label">Police Station</th>
                      <td>Bantra</td>
                    </tr>
                    <tr>
                      <th class="label">Post Office</th>
                      <td>Kadamtala</td>
                      <th class="label">Municipality Block</th>
                      <td>Howrah</td>
                    </tr>
                    <tr>
                      <th class="label">Assembly Constituency</th>
                      <td>Shibpur</td>
                      <th class="label">City</th>
                      <td>Howrah</td>
                    </tr>
                    <tr>
                      <th class="label">PIN</th>
                      <td>711101</td>
                      <th class="label"></th>
                      <td></td>
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
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Address Details</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Address</th>
                      <td>XYZ Test Address</td>
                      <th class="label">District</th>
                      <td>Howrah</td>
                    </tr>
                    <tr>
                      <th class="label">Sub Division</th>
                      <td>Howrah Sub</td>
                      <th class="label">Police Station</th>
                      <td>Bantra</td>
                    </tr>
                    <tr>
                      <th class="label">Post Office</th>
                      <td>Kadamtala</td>
                      <th class="label">Municipality Block</th>
                      <td>Howrah</td>
                    </tr>
                    <tr>
                      <th class="label">Assembly Constituency</th>
                      <td>Shibpur</td>
                      <th class="label">Gram Panchayat</th>
                      <td>XYZ</td>
                    </tr>
                    <tr>
                      <th class="label">PIN</th>
                      <td>711101</td>
                      <th class="label"></th>
                      <td></td>
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
                      <td colspan="3">{{ institutionPurpose.aimAndObjective.vision }}</td>
                    </tr>
                    <tr>
                      <th class="label">Mission</th>
                      <td colspan="3">{{ institutionPurpose.aimAndObjective.mission }}</td>
                    </tr>
                    <tr>
                      <th class="label">Core Values</th>
                      <td colspan="3">{{ institutionPurpose.aimAndObjective.coreValues }}</td>
                    </tr>
                    <tr>
                      <th class="label">Aims</th>
                      <td colspan="3">{{ institutionPurpose.aimAndObjective.aims }}</td>
                    </tr>
                    <tr>
                      <th class="label">Objective Concerned Institution</th>
                      <td colspan="3">To meet the growing demand for skilled engineers by offering state-of-the-art learning resources.</td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Institution Land Details</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Mouza</th>
                      <td>Mauza-A</td>
                      <th class="label">JlNo</th>
                      <td>159</td>
                    </tr>
                    <tr>
                      <th class="label">KhatianNo</th>
                      <td>1212</td>
                      <th class="label">Plot No</th>
                      <td>99/7B</td>
                    </tr>
                    <tr>
                      <th class="label">Area Clasification</th>
                      <td>1</td>
                      <th class="label"></th>
                      <td></td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Credibility And Readiness</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Experience In Education</th>
                      <td colspan="3">The trust has over 20 years of experience in running schools and training centers.</td>
                    </tr>
                    <tr>
                      <th class="label">General Reputation</th>
                      <td colspan="3">Recognized for its commitment to quality and community service in the region.</td>
                    </tr>
                    <tr>
                      <th class="label">Readiness To Comply With Regulatory Norms</th>
                      <td colspan="3">Fully committed to complying with regulatory norms set by the government and affiliating body.</td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Additional Commitments And Plans</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Student Reservation</th>
                      <td></td>
                      <th class="label">Employee Reservation</th>
                      <td></td>
                    </tr>
                    <tr>
                      <th class="label">Special Skill Development Activity</th>
                      <td></td>
                      <th class="label">Academic Auditing Plans</th>
                      <td></td>
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
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Total Number Of</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Class Room Count</th>
                      <td>10</td>
                      <th class="label">Seminar Room Count</th>
                      <td>2</td>
                    </tr>
                    <tr>
                      <th class="label">Multipurpose Hall Count</th>
                      <td>1</td>
                      <th class="label">Lab Resource Center Count</th>
                      <td>2</td>
                    </tr>
                    <tr>
                      <th class="label">ICT EduTech Lab Count</th>
                      <td>1</td>
                      <th class="label">Language Lab Count</th>
                      <td>2</td>
                    </tr>
                    <tr>
                      <th class="label">Store Room Count</th>
                      <td>1</td>
                      <th class="label">Boys CommonRoom Count</th>
                      <td>2</td>
                    </tr>
                    <tr>
                      <th class="label">Girls Common Room Count</th>
                      <td>1</td>
                      <th class="label">Boys Toilet Count</th>
                      <td>2</td>
                    </tr>
                    <tr>
                      <th class="label">Girls Toilet Count</th>
                      <td>1</td>
                      <th class="label"></th>
                      <td></td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Any Other Room</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Conferrence Room Status</th>
                      <td>1</td>
                      <th class="label">Meeting Room Status</th>
                      <td>2</td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Library Details</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Total Space</th>
                      <td>1</td>
                      <th class="label">Reading Room Count</th>
                      <td>2</td>
                    </tr>
                    <tr>
                      <th class="label">Books Count</th>
                      <td>1</td>
                      <th class="label">Journal Periodical Count</th>
                      <td>2</td>
                    </tr>
                    <tr>
                      <th class="label">Administrative Office Status</th>
                      <td>1</td>
                      <th class="label">Total Planned Construction</th>
                      <td>2</td>
                    </tr>
                    <tr>
                      <th class="label">College Covered Area</th>
                      <td>4</td>
                      <th class="label">College Land Area In Acres</th>
                      <td>2</td>
                    </tr>
                    <tr>
                      <th class="label">Comprehensive Plan</th>
                      <td colspan="3">In the next 5 years, we will expand the infrastructure, including hostels and recreational facilities.</td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Land Status</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Land Owned Status</th>
                      <td></td>
                      <th class="label">Land Converted For Educational Purpose Status</th>
                      <td></td>
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
                      <td>200000</td>
                      <th class="label">Source Of Fund</th>
                      <td>Bank Loan, Trust Funds, Government Grants</td>
                    </tr>
                    <tr>
                      <th class="label">Building Completion Status</th>
                      <td>Under Construction</td>
                      <th class="label">Building Completion Date</th>
                      <td>29-11-2025</td>
                    </tr>
                    <tr>
                      <th class="label">Building Plan Amount To Be Deposited</th>
                      <td>200000</td>
                      <th class="label">Nationalized Bank</th>
                      <td>State Bank of India</td>
                    </tr>
                    <tr>
                      <th class="label">Estimated Income And Expenditure For First 5 Years</th>
                      <td colspan="3">Projected income of 100000, projected expenditure of 80000</td>
                    </tr>
                    <tr>
                      <th class="label">Initial Fund Information</th>
                      <td colspan="3">Initial capital from trust and government subsidy.</td>
                    </tr>
                    <tr>
                      <th class="label" colspan="4" style="text-align: center;"><strong>Synopsis</strong></th>
                    </tr>
                    <tr>
                      <th class="label">Proposed Investment</th>
                      <td>500000</td>
                      <th class="label">Proposed Employment</th>
                      <td>200</td>
                    </tr>
                    <tr>
                      <th class="label">Professional Colleges Count Within 25 Km</th>
                      <td>5</td>
                      <th class="label">Feeder School Count With in 15 Km</th>
                      <td>10</td>
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
                    <tr>
                      <th class="label">Certificate of Registration of Societies West Bengal ACT XXVI of 1961</th>
                      <td>
                        <v-icon icon="mdi-check-circle" color="success" />
                      </td>
                      <th class="label">Details of Endowment Fund</th>
                      <td>
                        <v-icon icon="mdi-check-circle" color="success" />
                      </td>
                    </tr>
                    <tr>
                      <th class="label">Deed of Conveyance</th>
                      <td>
                        <v-icon icon="mdi-check-circle" color="success" />
                      </td>
                      <th class="label">Upload the document for the proof of land</th>
                      <td>
                        <v-icon icon="mdi-check-circle" color="success" />
                      </td>
                    </tr>
                    <tr>
                      <th class="label">Building Plan</th>
                      <td>
                        <v-icon icon="mdi-check-circle" color="success" />
                      </td>
                      <th class="label">Upload the proof of fees structure</th>
                      <td>
                        <v-icon icon="mdi-check-circle" color="success" />
                      </td>
                    </tr>
                  </tbody>
                </v-table>
              </v-card-text>
            </v-card>

            <!-- <v-alert variant="tonal" color="warning" class="mt-4">
              <div class="font-weight-medium mb-1">Self Declaration</div>
              <div class="text-body-2">
                I Shri/ Smt {{ applicantDetails.applicantName }} do hereby declare that I / my parents/ legal guardian/ my family have/ has been residing in the State of West Bengal since last 10 years (or more). I further declare that the above-mentioned information furnished by me is correct and true to my knowledge and belief.
              </div>
            </v-alert> -->
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const docketDialog = ref(false)
const docketNumber = ref('')

const saveDocketNumber = () => {
  // Persisting to API/store is not implemented here (not requested)
  docketDialog.value = false
}

const applicantDetails = {
  registrationNo: 'NOC20251218213221',
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
.label {
  width: 22%;
  font-weight: 600;
  white-space: nowrap;
}
</style>

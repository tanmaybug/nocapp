<template>
  <v-card elevation="2">
    <div class="table-heading">
      <div>
        <p class="fw-600 mb-0">Completed NOC Applications</p>
      </div>
      <div>
        <v-text-field v-model="search" density="compact" variant="outlined" label="Search" hide-details clearable class="search-field" />
      </div>
    </div>
    <v-divider />

    <v-data-table v-model:sort-by="sortBy" :headers="headers" :items="applications" :loading="loading" :search="search" item-value="registrationId" density="comfortable">
      <template #no-data>
        <div class="text-center text-grey-darken-1 py-6">No completed applications found.</div>
      </template>
    </v-data-table>
  </v-card>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { getCompletedApplications } from '../services'

type ApplicationRow = {
  registrationId: string | number
  institutionName: string
  applicantName: string
  applicantPhone: string
  applicantEmail: string
}

const headers = [
  { title: 'Registration Id', key: 'registrationId', sortable: true },
  { title: 'Institution Name', key: 'institutionName', sortable: true },
  { title: 'Applicant Name', key: 'applicantName', sortable: true },
  { title: 'Applicant Phone', key: 'applicantPhone', sortable: true },
  { title: 'Applicant Email', key: 'applicantEmail', sortable: true },
]

const sortBy = ref([{ key: 'registrationId', order: 'asc' as const }])
const search = ref('')
const applications = ref<ApplicationRow[]>([])
const loading = ref(false)

async function loadCompletedApplications() {
  loading.value = true
  try {
    applications.value = await getCompletedApplications()
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadCompletedApplications()
})
</script>

<style scoped>
.fw-600 {
  font-weight: 600;
}

.table-heading {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem;
}

.search-field {
  min-width: 260px;
}
</style>

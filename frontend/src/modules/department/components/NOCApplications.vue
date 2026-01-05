<template>
  <v-card elevation="2">
    <div class="d-flex flex-wrap align-center justify-space-between pa-6 ga-4">
      <div>
        <p class="font-weight-medium mb-0">NOC Applications</p>
      </div>
      <div class="d-flex flex-wrap align-center justify-end ga-3">
        <v-select v-model="selectedType" density="compact" variant="outlined" label="Type" hide-details style="min-width: 220px" :items="typeOptions" />
        <v-text-field v-model="search" density="compact" variant="outlined" label="Search" hide-details clearable style="min-width: 260px" />
      </div>
    </div>
    <v-divider />

    <v-data-table v-model:sort-by="sortBy" :headers="headers" :items="nocApplications.nocApplications" :loading="nocApplications.status === STATUS.PROCESSING" :search="search" item-value="registrationId" density="comfortable">
      <template #item.actions="{ item }">
        <v-btn variant="text" density="compact" :to="{ name: 'DepartmentNOCProfileView', params: { registrationId: item.registrationId } }" icon aria-label="View application" title="View application">
          <v-icon icon="mdi-eye" />
        </v-btn>
      </template>
      <template #no-data>
        <div class="text-center text-grey-darken-1 py-6">No applications found</div>
      </template>
    </v-data-table>
  </v-card>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { storeToRefs } from 'pinia'
import { useDepartmentStore } from '../stores'
import { NOC_APPLICATION_TYPE, type NOCApplicationType } from '../stores/departmentStore'
import { STATUS } from '@/types/common'

const route = useRoute()
const router = useRouter()

const departmentStore = useDepartmentStore()
const { nocApplications } = storeToRefs(departmentStore)

const headers = [
  { title: 'Registration Id', key: 'registrationId', sortable: true },
  { title: 'Institution Name', key: 'institutionName', sortable: true },
  { title: 'Applicant Name', key: 'applicantName', sortable: true },
  { title: 'Applicant Phone', key: 'applicantPhone', sortable: true },
  { title: 'Applicant Email', key: 'applicantEmail', sortable: true },
  { title: 'Action', key: 'actions', sortable: false },
]

const sortBy = ref([{ key: 'registrationId', order: 'asc' as const }])
const search = ref('')

const typeOptions = [
  { title: 'Pending', value: NOC_APPLICATION_TYPE.PENDING },
  { title: 'In-Process', value: NOC_APPLICATION_TYPE.IN_PROCESS },
  { title: 'Completed', value: NOC_APPLICATION_TYPE.COMPLETED },
]

const currentType = computed(() => route.params.type as NOCApplicationType)

const selectedType = computed<NOCApplicationType>({
  get: () => currentType.value,
  set: async (value) => {
    await router.push({ name: 'DepartmentNOCApplications', params: { type: value } })
  },
})

watch(
  () => route.params.type,
  async (raw) => {
    await departmentStore.getNOCApplicationsByStatus(raw as NOCApplicationType)
  },
  { immediate: true }
)
</script>

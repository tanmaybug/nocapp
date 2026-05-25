<template>
  <v-card elevation="2">
    <div class="d-flex flex-wrap align-center justify-space-between pa-6 ga-4">
      <div>
        <p class="font-weight-medium mb-0">Track NOC Application</p>
      </div>
      <div>
        <v-text-field v-model="search" density="compact" variant="outlined" label="Search" hide-details clearable style="min-width: 260px" />
      </div>
    </div>
    <v-divider />

    <v-data-table v-model:sort-by="sortBy" :headers="headers" :items="trackApplication" :search="search" :loading="status === 'processing'" item-value="sno" density="comfortable" hide-default-footer>
      <template #no-data>
        <div class="text-center text-grey-darken-1 py-6">No activity found.</div>
      </template>
    </v-data-table>
  </v-card>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useInstitutionStore } from '../stores'

const institutionStore = useInstitutionStore()
const { trackApplication, status } = storeToRefs(institutionStore)

const headers = [
  { title: 'S.No.', key: 'sno', sortable: true },
  { title: 'Activity', key: 'activity', sortable: true },
  { title: 'Date', key: 'date', sortable: true },
  { title: 'Remarks', key: 'remarks', sortable: true },
]

const sortBy = ref([{ key: 'sno', order: 'asc' as const }])
const search = ref('')

onMounted(() => {
  institutionStore.getTrackApplication()
})
</script>

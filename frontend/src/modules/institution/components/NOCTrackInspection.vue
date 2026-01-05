<template>
  <v-card elevation="2">
    <div class="d-flex flex-wrap align-center justify-space-between pa-6 ga-4">
      <div>
        <p class="font-weight-medium mb-0">Track Inspection</p>
      </div>
      <div>
        <v-text-field v-model="search" density="compact" variant="outlined" label="Search" hide-details clearable style="min-width: 260px" />
      </div>
    </div>
    <v-divider />

    <v-data-table v-model:sort-by="sortBy" :headers="headers" :items="inspectionFeedbacks" :search="search" item-value="sno" density="comfortable" hide-default-footer>
      <template #item.actions>
        <v-btn variant="text" density="compact" icon aria-label="View application" title="View Feedback">
          <v-icon icon="mdi-eye" />
        </v-btn>
      </template>
      <template #no-data>
        <div class="text-center text-grey-darken-1 py-6">No activity found.</div>
      </template>
    </v-data-table>
  </v-card>
</template>

<script setup lang="ts">
import { ref } from 'vue'

type TrackRow = {
  sno: number
  inspectionDate: string
  feedback: string
}

const headers = [
  { title: 'S.No.', key: 'sno', sortable: true },
  { title: 'Inspection Date', key: 'inspectionDate', sortable: true },
  { title: 'Feedback', key: 'feedback', sortable: true },
  { title: 'Action', key: 'actions', sortable: false },
]

const sortBy = ref([{ key: 'sno', order: 'asc' as const }])
const search = ref('')

const inspectionFeedbacks = ref<TrackRow[]>([
  {
    sno: 1,
    inspectionDate: '12-10-2025',
    feedback: 'Site visit completed. Land documents verified; no discrepancies observed.',
  },
  {
    sno: 2,
    inspectionDate: '14-10-2025',
    feedback: 'Infrastructure assessment done. Classrooms and lab space meet minimum requirements.',
  },
  {
    sno: 3,
    inspectionDate: '20-10-2025',
    feedback: 'Compliance review completed. Fire safety NOC copy requested for record update.',
  },
  {
    sno: 4,
    inspectionDate: '22-10-2025',
    feedback: 'Final remarks submitted. Recommended for next stage subject to document upload.',
  }
])
</script>

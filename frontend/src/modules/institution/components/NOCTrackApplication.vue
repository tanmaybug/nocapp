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

    <v-data-table v-model:sort-by="sortBy" :headers="headers" :items="activities" :search="search" item-value="sno" density="comfortable" hide-default-footer>
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
  activity: string
  date: string
  remarks: string
}

const headers = [
  { title: 'S.No.', key: 'sno', sortable: true },
  { title: 'Activity', key: 'activity', sortable: true },
  { title: 'Date', key: 'date', sortable: true },
  { title: 'Remarks', key: 'remarks', sortable: true },
]

const sortBy = ref([{ key: 'sno', order: 'asc' as const }])
const search = ref('')

const activities = ref<TrackRow[]>([
  {
    sno: 1,
    activity: 'Registration Done',
    date: '12-10-2025',
    remarks: '',
  },
  {
    sno: 2,
    activity: 'Final Submit Done',
    date: '14-10-2025',
    remarks: '',
  },
  {
    sno: 3,
    activity: 'Docket Number Added',
    date: '20-10-2025',
    remarks: '',
  },
  {
    sno: 4,
    activity: 'Inspection Date Assigned',
    date: '20-10-2025',
    remarks: '',
  },
])
</script>

<template>
  <v-row>
    <v-col cols="12">
      <h1 class="headline">Welcome back, {{ user!.name }}</h1>
    </v-col>
  </v-row>

  <v-row class="align-stretch">
    <v-col cols="12" md="8" lg="9" class="d-flex flex-column">
      <v-card class="pa-6" elevation="2" rounded="lg">
        <div class="d-flex align-start justify-space-between gap-4">
          <div>
            <p class="fw-600 text-grey-darken-1 mb-2">Current Status</p>
            <v-chip color="info" size="large" variant="tonal" class="text-none fw-600">
              {{ dashboardData.currentStatus }}
            </v-chip>
            <div class="d-flex align-center mt-3 text-body-2 text-grey-darken-1">
              <v-icon icon="mdi-clock-outline" size="16" class="mr-1" />
              <span>Updated on {{ dashboardData.lastUpdatedDate }}</span>
            </div>
          </div>

          <v-icon icon="mdi-file-document-outline" size="34" color="primary" />
        </div>
      </v-card>

      <v-card class="pa-6 mt-4" elevation="2" rounded="lg">
        <div class="d-flex align-start justify-space-between gap-4">
          <div>
            <p class="fw-600 text-grey-darken-1 mb-2">Inspection Date</p>
            <v-chip :color="dashboardData.inspectionDate ? 'info' : 'warning'" size="large" variant="tonal" class="text-none fw-600">
              {{ dashboardData.inspectionDate || 'Not Scheduled' }}
            </v-chip>
            <div class="d-flex align-center mt-3 text-body-2 text-grey-darken-1">
              <v-icon icon="mdi-calendar-clock-outline" size="16" class="mr-1" />
              <span>Inspection schedule for your application</span>
            </div>
          </div>

          <v-icon icon="mdi-calendar-month-outline" size="34" color="primary" />
        </div>
      </v-card>
    </v-col>
    <v-col cols="12" md="4" lg="3" class="d-flex">
      <v-card class="pa-4 flex-grow-1" elevation="2" rounded="lg">
        <div class="d-flex align-center justify-space-between mb-3">
          <p class="fw-600 mb-0">Quick Actions</p>
          <v-icon icon="mdi-lightning-bolt-outline" color="primary" />
        </div>
        <div class="d-flex flex-column gap-3">
          <v-btn v-for="action in actions" :key="action.label" class="text-none" :color="action.color" variant="outlined" @click="action.handler" :disabled="action?.isDisabled">
            <v-icon start :icon="action.icon" />
            {{ action.label }}
          </v-btn>
        </div>
      </v-card>
    </v-col>
  </v-row>

  <v-card class="mt-6" elevation="2">
    <div class="table-heading">
      <div>
        <p class="fw-600 mb-0">Recent Activities</p>
        <p class="text-body-2 text-grey-darken-1 mb-0">Stay up to date with actions taken on your application</p>
      </div>
      <v-btn text="Refresh" prepend-icon="mdi-refresh" variant="tonal" class="text-none" @click="loadDashboardData" />
    </div>
    <v-divider />
    <v-data-table v-model:sort-by="activitySortBy" :headers="activityHeaders" :items="dashboardData.activities" density="comfortable" item-value="sno" hide-default-footer>
      <template #item.sno="{ item }">
        <span class="fw-600">{{ item.sno }}</span>
      </template>

      <template #item.activity="{ item }">
        <p class="fw-600">{{ item.activity }}</p>
      </template>

      <template #item.status="{ item }">
        <v-chip :color="statusColorMap[item.status] ?? 'default'" size="small" class="text-none">{{ item.status }}</v-chip>
      </template>

      <template #item.date="{ item }">
        {{ item.date }}
      </template>

      <template #no-data>
        <div class="text-center text-grey-darken-1 py-6">No activities recorded yet.</div>
      </template>
    </v-data-table>
  </v-card>
</template>

<script setup lang="ts">
import router from '@/router'
import useAuthStore from '@/modules/auth/stores'
import { storeToRefs } from 'pinia'
import { computed, onMounted, ref } from 'vue'
import { useInstitutionStore, ACTIVITY_STATUS } from '../stores'

// Stores / base state
const institutionStore = useInstitutionStore()
const { dashboardData } = storeToRefs(institutionStore)
const { user } = storeToRefs(useAuthStore())

// Shared UI helpers
const statusColorMap: Record<string, string> = {
  [ACTIVITY_STATUS.PENDING]: 'warning',
  [ACTIVITY_STATUS.COMPLETED]: 'success'
}

// Quick Actions tile
const actions = computed(() => [
  {
    label: 'Edit Application',
    icon: 'mdi-pencil-outline',
    color: 'primary',
    handler: () => {
      router.push({ name: 'NOCApplication' })
    }
  },
  {
    label: 'View Application',
    icon: 'mdi-eye-outline',
    color: 'info',
    handler: () => {
      router.push({ name: 'NOCProfileView' })
    }
  },
  {
    label: 'Track Application',
    icon: 'mdi-timeline-clock-outline',
    color: 'default',
    handler: () => {
      router.push({ name: 'NOCTrackApplication' })
    }
  },
  {
    label: 'Track Inspection',
    icon: 'mdi-timeline-clock-outline',
    color: 'default',
    handler: () => {
      router.push({ name: 'NOCTrackInspection' })
    }
  },
  {
    label: 'NOC Doc Download',
    icon: 'mdi-file-download-outline',
    color: 'secondary',
    handler: () => { },
    isDisabled: !dashboardData.value.isNOCCompleted
  }
])

// Recent Activities table
const activityHeaders = [
  { title: 'S.No.', key: 'sno', sortable: true },
  { title: 'Activity', key: 'activity', sortable: true },
  { title: 'Status', key: 'status', sortable: true },
  { title: 'Date', key: 'date', sortable: true },
]
const activitySortBy = ref([{ key: 'sno', order: 'asc' as const }])

function loadDashboardData() {
  institutionStore.getDashboardData()
}


onMounted(() => {
  loadDashboardData()
})
</script>

<style scoped>
.fw-600 {
  font-weight: 600;
}

.gap-3 {
  gap: 0.75rem;
}

.gap-4 {
  gap: 1rem;
}

.action-chip {
  background: #eef4ff;
  color: #1a3fa3;
  border-radius: 999px;
  padding: 0.35rem 1rem;
  font-weight: 600;
  font-size: 0.9rem;
}

.table-heading {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem;
}
</style>

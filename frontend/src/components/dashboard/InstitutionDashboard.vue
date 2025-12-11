<template>
  <v-row>
    <v-col cols="12">
      <h1 class="headline">Welcome back, {{ user!.name }}</h1>
    </v-col>
  </v-row>

  <v-row>
    <v-col cols="12" md="8" lg="9">
      <v-card class="pa-6" elevation="2">
        <div class="d-flex flex-column flex-md-row align-md-center justify-space-between gap-4">
          <div>
            <p class="fw-600 text-grey-darken-1 mb-1">Current Status</p>
            <p class="text-h5 mb-0">{{ primaryStatus.title }}</p>
            <p class="text-body-2 text-grey-darken-1 mb-0">Updated on {{ primaryStatus.date }}</p>
          </div>
          <div class="action-chip">{{ primaryStatus.tag }}</div>
        </div>
      </v-card>
    </v-col>
    <v-col cols="12" md="4" lg="3">
      <v-card class="pa-4" elevation="2">
        <p class="fw-600 mb-3">Quick Actions</p>
        <div class="d-flex flex-column gap-3">
          <v-btn v-for="action in actions" :key="action.label" class="text-none" :color="action.color" variant="outlined" @click="action.handler">
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
      <v-btn text="Refresh" prepend-icon="mdi-refresh" variant="tonal" class="text-none" @click="onRefresh" />
    </div>
    <v-divider />
    <v-table density="comfortable">
      <thead>
        <tr>
          <th class="text-left">Sl. No</th>
          <th class="text-left">Activity</th>
          <th class="text-left">Status</th>
          <th class="text-left">Date</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in activities" :key="item.id">
          <td class="fw-600">{{ index + 1 }}</td>
          <td>
            <p class="mb-1 fw-600">{{ item.title }}</p>
            <p class="text-body-2 text-grey-darken-1 mb-0">{{ item.description }}</p>
          </td>
          <td>
            <v-chip :color="item.statusColor" size="small" class="text-none">{{ item.status }}</v-chip>
          </td>
          <td>{{ item.date }}</td>
        </tr>
        <tr v-if="!activities.length">
          <td colspan="4" class="text-center text-grey-darken-1 py-6">No activities recorded yet.</td>
        </tr>
      </tbody>
    </v-table>
  </v-card>
</template>

<script setup lang="ts">
import useAuthStore from '@/stores/authStore'
import { storeToRefs } from 'pinia'
import { computed } from 'vue'

const { user } = storeToRefs(useAuthStore())

const primaryStatus = {
  title: 'Application Under Review',
  tag: 'Awaiting Evaluation',
  date: '11 Dec 2025'
}

const activities = [
  {
    id: 1,
    title: 'Form 1 Submitted',
    description: 'You submitted general information for review.',
    status: 'Received',
    statusColor: 'primary',
    date: '08 Dec 2025'
  },
  {
    id: 2,
    title: 'Supporting Documents Uploaded',
    description: 'Document verification is in progress.',
    status: 'Processing',
    statusColor: 'warning',
    date: '09 Dec 2025'
  },
  {
    id: 3,
    title: 'Application Fee Acknowledged',
    description: 'Payment received via HED gateway.',
    status: 'Completed',
    statusColor: 'success',
    date: '10 Dec 2025'
  }
]

const actions = computed(() => [
  {
    label: 'View Application',
    icon: 'mdi-eye-outline',
    color: 'primary',
    handler: () => { }
  },
  {
    label: 'NOC Doc Download',
    icon: 'mdi-file-download-outline',
    color: 'secondary',
    handler: () => { }
  },
  {
    label: 'Track Application',
    icon: 'mdi-timeline-clock-outline',
    color: 'primary',
    handler: () => { }
  }
])

function onRefresh() {
}

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

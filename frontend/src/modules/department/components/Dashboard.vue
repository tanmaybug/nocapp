<template>
  <div class="admin-dashboard">
    <div class="cards-grid">
      <v-card v-for="card in cards" :key="card.title" variant="tonal" class="pa-4 card-panel">
        <div class="d-flex align-center justify-space-between mb-6">
          <v-icon :icon="card.icon" size="36" class="card-icon" />
        </div>
        <p class="eyebrow">{{ card.title }}</p>
        <h2 class="card-value">{{ card.value }}</h2>
        <v-btn variant="text" class="text-none px-0 mt-auto align-self-start" :text="card.actionText" :append-icon="'mdi-arrow-right'" @click="card.onAction" />
      </v-card>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useDepartmentStore } from '@/modules/department/stores'
import { computed } from 'vue'

// Stores / base state
const departmentStore = useDepartmentStore()

// Types
type CardType = {
  title: string
  value: string
  actionText: string
  icon: string
  onAction: () => void
}

// Computed
const cards = computed<CardType[]>(() => [
  {
    title: 'Total In-Process Applications',
    value: departmentStore.dashboardData.totalInProcessApplication.toString(),
    actionText: 'View details',
    icon: 'mdi-file-document-outline',
    onAction: () => { }
  },
  {
    title: 'Total Pending Reviews',
    value: departmentStore.dashboardData.totalPendingApplication.toString(),
    actionText: 'View details',
    icon: 'mdi-clipboard-text-clock-outline',
    onAction: () => { }
  },
  {
    title: 'Total NOC Complete Documents',
    value: departmentStore.dashboardData.totalNocCompleteApplication.toString(),
    actionText: 'View details',
    icon: 'mdi-shield-alert-outline',
    onAction: () => { }
  }
])

// Init
departmentStore.getDashboardData()
</script>

<style scoped>
.admin-dashboard {
  min-height: 100vh;
  background: linear-gradient(180deg, #f9fafc 0%, #ffffff 60%);
  padding: clamp(1.5rem, 4vw, 3rem);
}

.cards-grid {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
}

@media (min-width: 960px) {
  .cards-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

.card-panel {
  min-height: 100%;
  display: flex;
  flex-direction: column;
}

.eyebrow {
  min-height: 60px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 1rem;
  color: #64748b;
  margin-bottom: 0.35rem;
  font-weight: 600;
}

.card-icon {
  color: #3858d6;
}

.card-value {
  font-size: 2.5rem;
  margin: 0;
  color: #0f172a;
}
</style>
<template>
  <div class="admin-dashboard">
    <div class="cards-grid">
      <v-card v-for="card in cards" :key="card.title" variant="tonal" class="pa-4 card-panel">
        <div class="d-flex align-center justify-space-between mb-6">
          <v-icon :icon="card.icon" size="36" class="card-icon" />
          <v-chip :color="card.chipColor" size="small" class="text-none">{{ card.chipText }}</v-chip>
        </div>
        <p class="eyebrow">{{ card.subtitle }}</p>
        <h2 class="card-value">{{ card.value }}</h2>
        <p class="text-body-2 text-grey-darken-1 mb-6">{{ card.description }}</p>
        <v-btn variant="text" class="text-none px-0 mt-auto align-self-start" :text="card.actionText" :append-icon="'mdi-arrow-right'" @click="card.onAction" />
      </v-card>
    </div>
  </div>
</template>

<script setup lang="ts">
const cards = [
  {
    title: 'Applications',
    subtitle: 'Total applications',
    value: '1,248',
    description: 'Includes pending, approved, and rejected submissions this year.',
    actionText: 'View all applications',
    chipText: 'Live',
    chipColor: 'success',
    icon: 'mdi-file-document-outline',
    onAction: () => { }
  },
  {
    title: 'Reviews',
    subtitle: 'Pending reviews',
    value: '87',
    description: 'Items awaiting evaluation across all departments.',
    actionText: 'Open review queue',
    chipText: 'Attention',
    chipColor: 'warning',
    icon: 'mdi-clipboard-text-clock-outline',
    onAction: () => { }
  },
  {
    title: 'Compliance',
    subtitle: 'Documents flagged',
    value: '12',
    description: 'Applications requiring additional compliance documents.',
    actionText: 'Resolve now',
    chipText: 'Alerts',
    chipColor: 'error',
    icon: 'mdi-shield-alert-outline',
    onAction: () => { }
  }
]
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
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.75rem;
  color: #64748b;
  margin-bottom: 0.35rem;
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
<template>
  <div class="page dashboard-view">
    <v-container>
      <component :is="dashboardComponent" />
    </v-container>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import useAuthStore, { ROLE } from '@/stores/authStore'
import AdminDashboard from '@/components/dashboard/AdminDashboard.vue'
import InstitutionDashboard from '@/components/dashboard/InstitutionDashboard.vue'
import { storeToRefs } from 'pinia'

const { role } = storeToRefs(useAuthStore())
const dashboardComponent = computed(() => {
  const componentMap: Record<string, any> = {
    [ROLE.ADMIN]: AdminDashboard,
    [ROLE.INSTITUTION]: InstitutionDashboard,
  }
  return componentMap[role.value as string] || InstitutionDashboard
})
</script>

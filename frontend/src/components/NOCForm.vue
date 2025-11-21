<template>
  <v-container>
    <v-card>
      <v-card-title class="text-center">NOC Application Form</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="onSubmitTab" ref="formRef">
          <v-tabs v-model="activeTab" color="primary" grow>
            <v-tab v-for="tab in tabs" :key="tab.value" :value="tab.value"
              :class="{ 'tab-submitted': store.isTabSubmitted(tab.dataKey) }">
              <v-icon left>{{ tab.icon }}</v-icon>
              {{ NOC_FORM_LABEL_MAP[tab.dataKey] }}
              <v-icon v-if="store.isTabSubmitted(tab.dataKey)" class="ml-2" color="success" size="small">
                mdi-check-circle
              </v-icon>
            </v-tab>
          </v-tabs>
          <v-divider></v-divider>

          <!-- Tab Content -->
          <v-window v-model="activeTab">
            <v-window-item v-for="tab in tabs" :key="tab.value" :value="tab.value">
              <component :is="tab.component" :model-value="getTabData(tab)"
                @update:model-value="updateTabData(tab, $event)" :validation="validation" />
            </v-window-item>
          </v-window>

          <v-divider></v-divider>

          <!-- Navigation and Action Buttons -->
          <v-row class="mt-5">
            <v-col cols="12" class="d-flex justify-space-between align-center">
              <!-- Left side - Previous button -->
              <div>
                <v-btn v-if="canGoPrevious" variant="outlined" @click="goToPrevious">
                  <v-icon left>mdi-chevron-left</v-icon>
                  Previous
                </v-btn>
              </div>

              <!-- Right side - Next/Submit buttons -->
              <div>
                <v-btn color="primary" @click="onSubmitTab" :loading="store.status === 'processing'" class="mr-2">
                  Save
                </v-btn>

                <v-btn v-if="canGoNext" variant="outlined" @click="goToNext">
                  Next
                  <v-icon right>mdi-chevron-right</v-icon>
                </v-btn>

                <v-btn v-if="isLastTab && store.allTabsSubmitted" color="success" variant="flat"
                  @click="onSubmitComplete" :loading="store.status === 'processing'">
                  Complete Submission
                </v-btn>
              </div>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>
<script setup lang="ts">
import { ref, computed } from 'vue'
import { NOC_FORM_LABEL_MAP, useNOCStore } from '@/stores/nocStore'
import NOCForm1 from './noc-forms/NOCForm1.vue'
import NOCForm2 from './noc-forms/NOCForm2.vue'
import NOCForm3 from './noc-forms/NOCForm3.vue'

const store = useNOCStore()

const formRef = ref<any>(null)
const activeTab = ref(1)

// Tab configuration with components and navigation logic
const tabs = [
  {
    value: 1,
    icon: "mdi-information",
    component: NOCForm1,
    dataKey: 'form1'
  },
  {
    value: 2,
    icon: "mdi-currency-inr",
    component: NOCForm2,
    dataKey: 'form2'
  },
  {
    value: 3,
    icon: "mdi-upload",
    component: NOCForm3,
    dataKey: 'form3'
  }
]

// Computed properties for navigation
const currentTab = computed(() =>
  tabs.find(tab => tab.value === activeTab.value)
)

const isFirstTab = computed(() => activeTab.value === 1)
const isLastTab = computed(() => activeTab.value === tabs.length)
const canGoNext = computed(() => !isLastTab.value)
const canGoPrevious = computed(() => !isFirstTab.value)

// Validation state for child components
const validation = ref({
  isValid: true,
  errors: []
})

// Helper functions for dynamic component data binding
const getTabData = (tab: any) => {
  return store.getTabData(tab.dataKey)
}

const updateTabData = (tab: any, newValue: any) => {
  store.updateTabData(tab.dataKey, newValue)
}

// Navigation functions
const goToNext = () => {
  if (canGoNext.value) {
    activeTab.value++
  }
}

const goToPrevious = () => {
  if (canGoPrevious.value) {
    activeTab.value--
  }
}

// Tab submission
async function onSubmitTab() {
  const validation = await formRef.value.validate()
  if (!validation.valid) return

  const current = currentTab.value
  if (!current) return

  await store.submitTab(current.dataKey)
}

// Complete form submission
async function onSubmitComplete() {
  await store.submitCompleteForm()
}
</script>

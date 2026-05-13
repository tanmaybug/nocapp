<template>
  <v-row class="pa-2">
    <!-- 1. Projected Fund Flow -->
    <v-col cols="12">
      <div class="text-subtitle-1"><strong>Projected Fund Flow</strong></div>
    </v-col>

    <v-col cols="6">
      <v-text-field v-model="modelValue.projectedFundFlow.amount" label="Amount" type="number" step="0.01" prefix="₹" @input="updateValue" />
    </v-col>

    <v-col cols="6">
      <v-text-field v-model="modelValue.projectedFundFlow.sourceOfFund" label="Source of Fund" @input="updateValue" />
    </v-col>

    <!-- 2. Synopsis -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="12">
      <div class="text-subtitle-1"><strong>Synopsis</strong></div>
    </v-col>

    <v-col cols="6">
      <v-text-field v-model="modelValue.synopsis.proposedInvestment" label="Proposed Investment" @input="updateValue" />
    </v-col>

    <v-col cols="6">
      <v-text-field v-model="modelValue.synopsis.proposedEmployment" label="Proposed Employment" @input="updateValue" />
    </v-col>

    <v-col cols="6">
      <v-text-field v-model="modelValue.synopsis.professionalCollegesCountWithin25Km" label="Number of Professional Colleges within 25 kms" type="number" @input="updateValue" />
    </v-col>

    <v-col cols="6">
      <v-text-field v-model="modelValue.synopsis.feederSchoolCountWithin15Km" label="Number of Feeder school in the region within 15 kms" type="number" @input="updateValue" />
    </v-col>

    <!-- 3. Building Completion Status -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="6">
      <div class="text-body-2 mb-2">Whether the building is completed</div>
      <v-radio-group v-model="modelValue.buildingCompletionStatus" row @update:model-value="updateValue">
        <v-radio v-for="option in yesNoOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <!-- 4. Building Completion Date (conditional) -->
    <v-col cols="6" v-if="modelValue.buildingCompletionStatus === '1'">
      <v-text-field v-model="modelValue.buildingCompletionDate" label="Date of Completion of the Building" type="date" @input="updateValue" />
    </v-col>

    <v-col cols="6" v-else-if="modelValue.buildingCompletionStatus === '0'">
      <v-text-field v-model="modelValue.buildingCompletionExpectedDate" label="Expected Date of Completion of the Building" type="date" @input="updateValue" />
    </v-col>

    <!-- 5. Building Plan Amount to be Deposited -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="12">
      <div class="text-body-2 mb-2">Application Fees to be deposited to HED</div>
      <v-radio-group v-model="modelValue.buildingPlanAmountToBeDeposited" @update:model-value="updateValue">
        <v-radio v-for="option in buildingPlanAmountOptions" :key="option.value" :label="option.label" :value="option.value" />
      </v-radio-group>
    </v-col>

    <!-- 6. Estimated Income and Expenditure -->
    <v-col cols="12">
      <v-divider class="my-4"></v-divider>
    </v-col>
    <v-col cols="12">
      <v-textarea v-model="modelValue.estimatedIncomeAndExpenditureForFirst5Years" label="Estimated Income and Expenditure for the first 5 years" rows="4" @input="updateValue" />
    </v-col>

    <!-- 7. Initial Fund Information -->
    <v-col cols="6">
      <v-textarea v-model="modelValue.initialFundInformation" label="Information about the initial fund" rows="1" @input="updateValue" />
    </v-col>

    <!-- 8. Nationalized Bank -->
    <v-col cols="6">
      <v-select v-model="modelValue.nationalizedBank" label="Nationalized Bank" :items="nationalizedBankOptions" item-title="label" item-value="value" @update:model-value="updateValue" />
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import type { PropType } from 'vue'

// Props
type ModelValue = {
  projectedFundFlow: {
    amount: string
    sourceOfFund: string
  }
  synopsis: {
    proposedInvestment: string
    proposedEmployment: string
    professionalCollegesCountWithin25Km: number
    feederSchoolCountWithin15Km: number
  }
  buildingCompletionStatus: string
  buildingCompletionDate: string
  buildingCompletionExpectedDate: string
  buildingPlanAmountToBeDeposited: string
  estimatedIncomeAndExpenditureForFirst5Years: string
  initialFundInformation: string
  nationalizedBank: string
}

const { modelValue } = defineProps({
  modelValue: { type: Object as PropType<ModelValue>, required: true },
})

// Emits
const emit = defineEmits<{
  'update:modelValue': [value: any]
}>()

// Options for radio buttons
const yesNoOptions = [
  { label: 'Yes', value: '1' },
  { label: 'No', value: '0' }
]

const buildingPlanAmountOptions = [
  { label: '₹1,00,000 Fresh, urban/metro', value: '1' },
  { label: '₹50,000 Fresh, Rural', value: '2' },
  { label: '₹50,000 Existing Gov-aided, urban/metro', value: '3' },
  { label: '₹25,000 Existing Gov-aided, Rural', value: '4' }
]

const nationalizedBankOptions = [
  { label: 'State Bank of India', value: 'sbi' },
  { label: 'Punjab National Bank', value: 'pnb' },
  { label: 'Bank of Baroda', value: 'bob' },
  { label: 'Canara Bank', value: 'canara' },
  { label: 'Union Bank of India', value: 'union' },
  { label: 'Bank of India', value: 'boi' },
  { label: 'Central Bank of India', value: 'central' },
  { label: 'Indian Bank', value: 'indian' },
  { label: 'Indian Overseas Bank', value: 'iob' },
  { label: 'UCO Bank', value: 'uco' },
  { label: 'Bank of Maharashtra', value: 'bom' },
  { label: 'Punjab & Sind Bank', value: 'psb' }
]

function updateValue() {
  emit('update:modelValue', modelValue)
}
</script>

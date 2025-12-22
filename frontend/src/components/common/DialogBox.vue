<template>
  <v-dialog width="500" v-model="isVisible" persistent>
    <v-card :title="currentDialog?.title">
      <v-card-text v-html="currentDialog?.message"></v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn v-if="currentDialog?.type === 'CONFIRM'" text="Confirm" @click="onConfirm"></v-btn>
        <v-btn :text="closeDialogLabel" @click="onClose"></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { useDialogStore, type DialogType } from '@/stores/dialogStore'
import { storeToRefs } from 'pinia'
import { computed } from 'vue'

// Stores / base state
const dialogStore = useDialogStore()
const { isVisible, currentDialog } = storeToRefs(dialogStore)

// Computed
const closeDialogLabel = computed(() => {
  const closeDialogLabelMap: Record<DialogType, string> = {
    ALERT: 'Close',
    CONFIRM: 'Cancel'
  }
  return closeDialogLabelMap[currentDialog.value?.type as DialogType]
})

// Handlers
function onClose() {
  dialogStore.hideDialog()
  currentDialog.value?.onCancel?.()
}
function onConfirm() {
  dialogStore.hideDialog()
  currentDialog.value?.onConfirm?.()
}
</script>
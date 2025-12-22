<template>
  <v-row>
    <v-col cols="8">
      <p class="mb-0">{{ label }}</p>
    </v-col>
    <v-col cols="4" class="text-right">
      <v-btn class="ms-2" variant="flat" color="primary" @click="showFileUploadDialog = true">Add/Edit file(s)</v-btn>
    </v-col>
  </v-row>
  <v-dialog v-model="showFileUploadDialog" width="820" min-height="500">
    <v-card width="800" class="upload-panel">
      <v-row class="pa-0 upload-panel__input-row">
        <v-col cols="12">
          <p class="mb-2">{{ label }}</p>
        </v-col>
        <v-col cols="12">
          <div class="upload-panel__input-wrapper">
            <v-file-input prepend-icon="" class="flex-grow-1" v-model="selectedFile" label="Choose a file" :show-size="showSize" :rules="rules" :accept="getAcceptAttribute()" counter :chips="showChips" :hint="inputHint" persistent-hint />
            <v-btn variant="flat" color="primary" class="text-none mb-4" :disabled="!selectedFile || draftFiles.length >= maxFiles" @click="onAdd">
              Upload file
            </v-btn>
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <div class="upload-panel__list-header">
            <div>
              <p class="list-title mb-0">Uploaded {{ maxFiles === 1 ? 'file' : 'files' }}</p>
            </div>
            <v-chip v-if="showCount" variant="outlined" color="grey">{{ draftFiles?.length || 0 }} uploaded</v-chip>
          </div>
          <v-card class="upload-panel__list">
            <v-list v-if="draftFiles.length" lines="two">
              <v-list-item v-for="(file, index) in draftFiles" :key="(file.id || file.name || file.originalName) + '-' + index" class="upload-panel__list-item" :disabled="!draftFiles">
                <template #prepend>
                  <v-avatar color="primary" variant="tonal" class="me-3" size="36">
                    <span class="text-caption text-uppercase">{{ getFileExtension(file) }}</span>
                  </v-avatar>
                </template>
                <v-list-item-title class="fw-600">{{ file.originalName || file.name }}</v-list-item-title>
                <v-list-item-subtitle>{{ formatBytes(file.size) }}</v-list-item-subtitle>
                <template #append>
                  <div v-if="draftFiles" class="d-flex align-center">
                    <v-btn v-if="getFileUrl(file)" icon="mdi-eye" variant="text" color="primary" class="me-1" @click="onPreview(file)" />
                    <v-btn color="grey-darken-1" icon="mdi-close" variant="text" @click="onRemove(index)" />
                  </div>
                </template>
              </v-list-item>
            </v-list>
            <div v-else class="text-center py-6 text-grey-darken-1 text-body-2">No files uploaded yet.</div>
          </v-card>
        </v-col>
      </v-row>

      <v-card-actions class="pt-6">
        <v-spacer />
        <v-btn variant="text" class="text-none" @click="onCancel">Cancel</v-btn>
        <v-btn variant="flat" color="primary" class="text-none" :disabled="!hasPendingChanges" @click="onSave">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import { formatBytes } from '@/composables/helpers'
import useDialogStore from '@/stores/dialogStore'

const dialogStore = useDialogStore()
const { label, uploadedFiles, showSize, showCount, maxFiles, acceptedTypes, rules, showChips, hint } = defineProps({
  label: { type: String, default: 'Upload file' },
  uploadedFiles: {
    type: Array as () => any[],
    default: () => [],
  },
  showSize: { type: Boolean, default: true },
  showCount: { type: Boolean, default: false },
  maxFiles: { type: Number, default: 1 },
  acceptedTypes: { type: Array as () => string[], default: () => ['PDF'] },
  rules: { type: Array as () => any[], default: () => [] },
  showChips: { type: Boolean, default: false },
  hint: { type: String, default: '' }
})
const emit = defineEmits(['add', 'remove', 'save', 'cancel'])
const selectedFile = ref<File | null>(null)
const showFileUploadDialog = ref<boolean>(false)
const inputHint = computed(() => hint || (maxFiles > 1 ? `Upload up to ${maxFiles} files (${acceptedTypes.join(', ')})` : `Accepted formats: ${acceptedTypes.join(', ')}`))
const draftFiles = ref<any[]>([])
const originalFilesSnapshot = ref<any[]>([])
const pendingAdds = ref<File[]>([])
const pendingRemoveIds = ref<Set<string>>(new Set())

const hasPendingChanges = computed(() => pendingAdds.value.length > 0 || pendingRemoveIds.value.size > 0)

function getFileStableId(file: any): string {
  return String(file?.id || file?.originalName || file?.name || '')
}

function syncDraftFromProps() {
  originalFilesSnapshot.value = Array.isArray(uploadedFiles) ? [...uploadedFiles] : []
  draftFiles.value = [...originalFilesSnapshot.value]
  pendingAdds.value = []
  pendingRemoveIds.value = new Set()
  selectedFile.value = null
}

// Generate accept attribute for file input
function getAcceptAttribute(): string {
  const mimeTypes: Record<string, string> = {
    'PDF': '.pdf,application/pdf',
    'DOC': '.doc,application/msword',
    'DOCX': '.docx,application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'JPG': '.jpg,.jpeg,image/jpeg',
    'JPEG': '.jpg,.jpeg,image/jpeg',
    'PNG': '.png,image/png'
  }

  const acceptValues = acceptedTypes
    .map(type => mimeTypes[type.toUpperCase()])
    .filter(Boolean)
    .join(',')

  return acceptValues
}

// File type validation function
function validateFileType(file: File): boolean {
  if (!file) return false

  const fileExtension = file.name.split('.').pop()?.toUpperCase()
  if (!fileExtension) return false

  return acceptedTypes.map(type => type.toUpperCase()).includes(fileExtension)
}

function onAdd() {
  if (!selectedFile.value || draftFiles.value.length >= maxFiles) return

  // Validate file type
  if (!validateFileType(selectedFile.value)) {
    dialogStore.showDialog({
      type: 'ALERT',
      title: 'Invalid File Type',
      message: `Accepted formats: ${acceptedTypes.join(', ')}`
    })
    return
  }

  pendingAdds.value.push(selectedFile.value)
  draftFiles.value.push({
    __pending: true,
    name: selectedFile.value.name,
    originalName: selectedFile.value.name,
    size: selectedFile.value.size,
  })

  selectedFile.value = null
}

function onRemove(index: number) {
  const file = draftFiles.value[index]
  if (!file) return

  if (file.__pending) {
    const pendingIndex = pendingAdds.value.findIndex(f => f.name === file.name && f.size === file.size)
    if (pendingIndex >= 0) pendingAdds.value.splice(pendingIndex, 1)
    draftFiles.value.splice(index, 1)
    return
  }

  const id = getFileStableId(file)
  if (id) pendingRemoveIds.value.add(id)
  draftFiles.value.splice(index, 1)
}

function getFileUrl(file: any): string | null {
  if (file?.__pending) return null
  return file?.url || file?.previewUrl || file?.path || null
}

function getFileExtension(file: any): string {
  const name = file?.originalName || file?.name || ''
  const extension = name.split('.').pop()
  return (extension || 'FILE').slice(0, 3).toUpperCase()
}

function onPreview(file: any) {
  const url = getFileUrl(file)
  if (url) {
    window.open(url, '_blank', 'noopener')
    return
  }

  dialogStore.showDialog({
    type: 'ALERT',
    title: 'Preview Unavailable',
    message: 'This file does not have a previewable link yet.'
  })
}

function onCancel() {
  emit('cancel')
  syncDraftFromProps()
  showFileUploadDialog.value = false
}

function onSave() {
  // Apply removals first (based on the original snapshot)
  const removedIds = pendingRemoveIds.value
  if (removedIds.size > 0) {
    const itemsToRemove = originalFilesSnapshot.value.filter(f => removedIds.has(getFileStableId(f)))
    for (const item of itemsToRemove) {
      const indexInCurrent = uploadedFiles.findIndex(f => getFileStableId(f) === getFileStableId(item))
      if (indexInCurrent >= 0) emit('remove', indexInCurrent)
    }
  }

  // Then apply adds
  for (const file of pendingAdds.value) {
    emit('add', file)
  }

  emit('save')
  showFileUploadDialog.value = false
}

watch(showFileUploadDialog, (open) => {
  if (open) syncDraftFromProps()
  if (!open) selectedFile.value = null
})
</script>

<style scoped>
.upload-panel {
  padding: 32px;
  border-radius: 24px;
  box-shadow: 0 20px 45px rgba(15, 23, 42, 0.12);
}

.upload-panel__input-row {
  gap: 1rem;
}

.upload-panel__input-wrapper {
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  gap: 1rem;
  flex-wrap: wrap;
}

.upload-panel__input-wrapper .v-btn {
  align-self: center;
  min-width: 140px;
}

.upload-panel__list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  margin-bottom: 0.75rem;
}

.upload-panel__list-item {
  border-bottom: 1px solid rgba(148, 163, 184, 0.25);
}

.upload-panel__list-item:last-of-type {
  border-bottom: none;
}

.fw-600 {
  font-weight: 600;
}

@media (max-width: 600px) {
  .upload-panel {
    padding: 20px;
  }

  .upload-panel__input-wrapper {
    flex-direction: column;
    align-items: stretch;
  }

}
</style>

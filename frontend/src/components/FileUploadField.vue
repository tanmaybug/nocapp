<template>
  <v-btn class="ms-2" variant="outlined" @click="showFileUploadDialog = true">Add/Edit file(s)</v-btn>
  <v-dialog v-model="showFileUploadDialog" width="820" min-height="500">
    <v-card width="800" class="upload-panel">
      <div class="upload-panel__header">
        <div class="upload-panel__header-spacer"></div>
        <div class="upload-panel__header-actions">
          <v-btn icon="mdi-close" variant="text" @click="showFileUploadDialog = false" />
        </div>
      </div>
      <v-row class="pa-0 upload-panel__input-row">
        <v-col cols="12">
          <p class="mb-2">{{ label }}</p>
        </v-col>
        <v-col cols="12">
          <div class="upload-panel__input-wrapper">
            <v-file-input prepend-icon="" class="flex-grow-1" v-model="selectedFile" label="Choose a file" :show-size="showSize" :rules="rules" :accept="getAcceptAttribute()" counter :chips="showChips" :hint="inputHint" persistent-hint />
            <v-btn variant="flat" color="primary" class="text-none mb-4" :disabled="!selectedFile || uploadedFiles.length >= maxFiles" @click="onAdd">
              Upload file
            </v-btn>
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <div class="upload-panel__list-header">
            <div>
              <p class="list-title mb-0">Uploaded files</p>
            </div>
            <v-chip v-if="showCount" variant="outlined" color="grey">{{ uploadedFiles?.length || 0 }} uploaded</v-chip>
          </div>
          <v-card variant="outlined" class="upload-panel__list">
            <v-list variant="outlined" v-if="uploadedFiles.length" lines="two">
              <v-list-item v-for="(file, index) in uploadedFiles" :key="(file.id || file.name || file.originalName) + '-' + index" class="upload-panel__list-item" :disabled="!uploadedFiles">
                <template #prepend>
                  <v-avatar color="primary" variant="tonal" class="me-3" size="36">
                    <span class="text-caption text-uppercase">{{ getFileExtension(file) }}</span>
                  </v-avatar>
                </template>
                <v-list-item-title class="fw-600">{{ file.originalName || file.name }}</v-list-item-title>
                <v-list-item-subtitle>{{ formatBytes(file.size) }}</v-list-item-subtitle>
                <template #append>
                  <div v-if="uploadedFiles" class="d-flex align-center">
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

      <template #actions />
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { formatBytes } from '@/composables/helpers'
import useDialogStore from '@/stores/dialogStore'

const dialogStore = useDialogStore()

const { label, uploadedFiles, showSize, showCount, maxFiles, acceptedTypes, rules, showChips, hint } = defineProps({
  label: { type: String, default: 'Upload file' },
  uploadedFiles: {
    type: Array as () => any[], default: () => [
      {
        id: 'demo-1',
        originalName: 'Proposal for campus development programme.pdf',
        size: 524288
      },
      {
        id: 'demo-2',
        originalName: 'Financial_projection.xlsx',
        size: 262144
      },
      {
        id: 'demo-3',
        originalName: 'Site_photos.zip',
        size: 734003
      }
    ]
  },
  showSize: { type: Boolean, default: true },
  showCount: { type: Boolean, default: false },
  maxFiles: { type: Number, default: 1 },
  acceptedTypes: { type: Array as () => string[], default: () => ['PDF', 'DOC', 'DOCX', 'JPG', 'JPEG', 'PNG'] },
  rules: { type: Array as () => any[], default: () => [] },
  showChips: { type: Boolean, default: false },
  hint: { type: String, default: '' }
})

const emit = defineEmits(['add', 'remove'])

const selectedFile = ref<File | null>(null)
const showFileUploadDialog = ref<boolean>(false)
const inputHint = computed(() => hint || (maxFiles > 1 ? `Upload up to ${maxFiles} files (${acceptedTypes.join(', ')})` : `Accepted formats: ${acceptedTypes.join(', ')}`))

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
  if (!selectedFile.value || uploadedFiles.length >= maxFiles) return

  // Validate file type
  if (!validateFileType(selectedFile.value)) {
    dialogStore.showDialog({
      type: 'ALERT',
      title: 'Invalid File Type',
      message: `Accepted formats: ${acceptedTypes.join(', ')}`
    })
    return
  }

  emit('add', selectedFile.value)
  selectedFile.value = null
}

function onRemove(index: number) {
  emit('remove', index)
}

function getFileUrl(file: any): string | null {
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
</script>

<style scoped>
.upload-panel {
  padding: 32px;
  border-radius: 24px;
  box-shadow: 0 20px 45px rgba(15, 23, 42, 0.12);
}

.upload-panel__header {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 1rem;
}

.upload-panel__header-spacer {
  flex: 1;
}

.upload-panel__header-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
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

  .upload-panel__input-wrapper,
  .upload-panel__header {
    flex-direction: column;
    align-items: stretch;
  }

}
</style>

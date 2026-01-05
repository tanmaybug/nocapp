<template>
  <v-row>
    <v-col cols="8" class="d-flex align-center">
      <p class="font-weight-medium">{{ label }}</p>
    </v-col>
    <v-col cols="4" class="text-right">
      <v-btn class="ms-2" variant="flat" color="primary" @click="showFileUploadDialog = true">Add/Edit file(s)</v-btn>
    </v-col>
  </v-row>
  <v-dialog v-model="showFileUploadDialog" width="820" min-height="500" persistent>
    <v-card width="800" class="pa-8 elevation-10">
      <v-row class="pa-0">
        <v-col cols="12">
          <p class="mb-2 font-weight-medium">{{ label }}</p>
        </v-col>
        <v-col cols="12">
          <div class="d-flex flex-column flex-sm-row flex-wrap align-stretch align-sm-end ga-4">
            <v-file-input prepend-icon="" class="flex-grow-1" v-model="selectedFile" label="Choose a file" :show-size="showSize" :rules="rules" :accept="getAcceptAttribute()" counter :chips="showChips" :hint="inputHint" persistent-hint />
            <v-btn variant="flat" color="primary" class="text-none mb-8" :loading="isUploading" :disabled="!selectedFile || internalFiles.length >= maxFiles || isUploading" @click="onUpload">
              Upload file
            </v-btn>
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <div class="d-flex justify-space-between align-center ga-4 mb-3">
            <div>
              <p class="list-title mb-0">Uploaded {{ maxFiles === 1 ? 'file' : 'files' }}</p>
            </div>
            <v-chip v-if="showCount" variant="outlined" color="grey">{{ internalFiles.length || 0 }} uploaded</v-chip>
          </div>
          <v-card class="upload-panel__list">
            <v-list v-if="internalFiles.length" lines="two">
              <v-list-item v-for="(file, index) in internalFiles" :key="(file.fileId || file.id || file.name || file.originalName) + '-' + index" :class="index !== internalFiles.length - 1 ? 'border-b' : ''">
                <template #prepend>
                  <v-avatar color="primary" variant="tonal" class="me-3" size="36">
                    <span class="text-caption text-uppercase">{{ getFileExtension(file) }}</span>
                  </v-avatar>
                </template>
                <v-list-item-title class="font-weight-medium">{{ file.originalName || file.name }}</v-list-item-title>
                <v-list-item-subtitle>{{ formatBytes(file.size) }}</v-list-item-subtitle>
                <template #append>
                  <div class="d-flex align-center">
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
        <v-btn variant="flat" color="primary" class="text-none" :loading="isSaving" :disabled="isSaving || internalFiles.length === 0" @click="onSave">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import { formatBytes } from '@/composables/helpers'
import useDialogStore from '@/stores/dialogStore'
import { uploadFile as fileUpload, saveFile as fileSave } from '@/modules/institution/services/institution.service'

const dialogStore = useDialogStore()
const { label, uploadedFiles, showSize, showCount, maxFiles, acceptedTypes, rules, showChips, hint, documentId, documentType } = defineProps({
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
  ,
  documentId: { type: Number, default: 0 },
  documentType: { type: String, default: '' }
})
const emit = defineEmits(['update:uploadedFiles', 'save', 'cancel'])
const selectedFile = ref<File | null>(null)
const showFileUploadDialog = ref<boolean>(false)
const inputHint = computed(() => hint || (maxFiles > 1 ? `Upload up to ${maxFiles} files (${acceptedTypes.join(', ')})` : `Accepted formats: ${acceptedTypes.join(', ')}`))
const internalFiles = ref<any[]>([])
const isUploading = ref(false)
const isSaving = ref(false)

const effectiveDocumentType = computed(() => documentType || label)

function normalizeIncomingFile(file: any) {
  if (!file) return null
  return {
    ...file,
    originalName: file.originalName || file.name || file.fileName,
    name: file.name || file.originalName || file.fileName,
    size: file.size ?? 0,
    fileId: file.fileId ?? file.id,
    fileUrl: file.fileUrl || file.url || file.previewUrl || file.path,
    __saved: file.__saved ?? true,
  }
}

function syncFromProps() {
  internalFiles.value = (Array.isArray(uploadedFiles) ? uploadedFiles : [])
    .map(normalizeIncomingFile)
    .filter(Boolean)
}

function emitFilesUpdate() {
  emit('update:uploadedFiles', [...internalFiles.value])
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

function onUpload() {
  if (!selectedFile.value || internalFiles.value.length >= maxFiles) return

  if (isUploading.value) return

  // Validate file type
  if (!validateFileType(selectedFile.value)) {
    dialogStore.showDialog({
      type: 'ALERT',
      title: 'Invalid File Type',
      message: `Accepted formats: ${acceptedTypes.join(', ')}`
    })
    return
  }

  const fileToUpload = selectedFile.value
  isUploading.value = true
  fileUpload(fileToUpload)
    .then((resp: any) => {
      const uploaded = resp?.fileId ? resp : resp?.data
      if (!uploaded) throw new Error('Upload succeeded but returned no file data')

      internalFiles.value.push({
        ...uploaded,
        originalName: fileToUpload.name,
        name: fileToUpload.name,
        size: fileToUpload.size,
        __saved: false,
      })

      emitFilesUpdate()

      selectedFile.value = null
    })
    .catch((err: any) => {
      dialogStore.showDialog({
        type: 'ALERT',
        title: 'Upload Failed',
        message: err?.response?.data?.detail || err?.response?.data?.message || err?.message || 'File upload failed. Please try again.',
      })
    })
    .finally(() => {
      isUploading.value = false
    })
}

function onRemove(index: number) {
  const file = internalFiles.value[index]
  if (!file) return

  internalFiles.value.splice(index, 1)
  emitFilesUpdate()
}

function getFileUrl(file: any): string | null {
  return file?.fileUrl || file?.url || file?.previewUrl || file?.path || null
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
  showFileUploadDialog.value = false
}

async function onSave() {
  if (isSaving.value) return

  const pending = internalFiles.value.filter((f: any) => f && f.__saved === false)
  if (pending.length === 0) {
    emit('save')
    showFileUploadDialog.value = false
    return
  }

  if (!documentId) {
    emit('save')
    showFileUploadDialog.value = false
    return
  }

  isSaving.value = true
  try {
    for (const file of pending) {
      const fileId = Number(file.fileId ?? file.id)
      if (!fileId) continue

      await fileSave({
        fileId,
        documentType: effectiveDocumentType.value,
        documentTypeId: Number(documentId),
      })

      file.__saved = true
    }

    emitFilesUpdate()

    emit('save')
    showFileUploadDialog.value = false
  } catch (err: any) {
    dialogStore.showDialog({
      type: 'ALERT',
      title: 'Save Failed',
      message: err?.response?.data?.detail || err?.response?.data?.message || err?.message || 'File save failed. Please try again.',
    })
  } finally {
    isSaving.value = false
  }
}

watch(showFileUploadDialog, (open) => {
  if (open) syncFromProps()
  if (!open) selectedFile.value = null
})

watch(() => uploadedFiles, () => {
  syncFromProps()
}, { deep: true, immediate: true })
</script>

<style scoped></style>

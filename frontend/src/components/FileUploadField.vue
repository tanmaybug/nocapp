<template>
  <div>
    <v-row class="pa-0">
      <v-col cols="12" class="d-flex align-center">
        <v-file-input 
          class="flex-grow-1" 
          v-model="selectedFile" 
          :label="label" 
          :show-size="showSize" 
          :rules="rules"
          :accept="getAcceptAttribute()"
        />
        <v-btn class="ms-2" variant="outlined" :disabled="!selectedFile || uploadedFiles.length >= maxFiles" @click="onAdd">Add file</v-btn>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <v-label class="mb-3" v-show="showCount">Uploaded ({{ uploadedFiles?.length || 0 }})</v-label>
        <v-card>
          <v-list dense v-if="uploadedFiles && uploadedFiles.length">
            <v-list-item v-for="(file, index) in uploadedFiles" :key="file.name + '-' + index">
              <v-list-item-title>{{ file.originalName }}</v-list-item-title>
              <v-list-item-subtitle>{{ formatBytes(file.size) }}</v-list-item-subtitle>
              <template v-slot:append>
                <v-btn color="grey-lighten-1" icon="mdi-close" variant="text" @click="onRemove(index)"></v-btn>
              </template>
            </v-list-item>
          </v-list>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { formatBytes } from '@/composables/helpers'
import useDialogStore from '@/stores/dialogStore'

const dialogStore = useDialogStore()

const { label, uploadedFiles, showSize, showCount, maxFiles, acceptedTypes, rules } = defineProps({
  label: { type: String, default: 'Upload file' },
  uploadedFiles: { type: Array as () => any[], default: () => [] },
  showSize: { type: Boolean, default: true },
  showCount: { type: Boolean, default: false },
  maxFiles: { type: Number, default: 1 },
  acceptedTypes: { type: Array as () => string[], default: () => ['PDF', 'DOC', 'DOCX', 'JPG', 'JPEG', 'PNG'] },
  rules: { type: Array as () => any[], default: () => [] }
})

const emit = defineEmits(['add', 'remove'])

const selectedFile = ref<File | null>(null)

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
</script>

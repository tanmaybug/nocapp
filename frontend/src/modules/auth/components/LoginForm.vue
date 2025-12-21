<template>
  <v-card>
    <v-card-title class="text-center my-2">Login</v-card-title>
    <v-card-text>
      <v-form ref="formRef" @submit.prevent="onSubmit">
        <v-row class="px-2">
          <v-col cols="12">
            <v-text-field v-model="form.username" label="Username *" :rules="[requiredRule]" autocomplete="username" tabindex="1" />
          </v-col>
          <v-col cols="12">
            <v-text-field v-model="form.password" label="Password *" :rules="[requiredRule, passwordRule]" :type="showPassword ? 'text' : 'password'" :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'" @click:append-inner="showPassword = !showPassword" autocomplete="current-password" tabindex="2" @keydown.enter="onSubmit" />
          </v-col>
          <v-col v-if="error" cols="12">
            <v-alert type="error" variant="tonal" density="comfortable">
              {{ error }}
            </v-alert>
          </v-col>
          <v-col cols="12" class="d-flex justify-end">
            <v-btn variant="text" @click="onReset">Reset</v-btn>
            <v-btn class="ms-2" :disabled="false" @click="onSubmit" color="primary" tabindex="3">Login</v-btn>
          </v-col>
        </v-row>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { requiredRule, passwordRule } from '@/composables/validators'
import { useAuthStore } from '@/modules/auth/stores'
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'

const store = useAuthStore()
const { form, error } = storeToRefs(store)
const router = useRouter()
const formRef = ref<any>(null)
const showPassword = ref(false)

async function onSubmit() {
  if (!formRef.value) return

  const validation = await formRef.value.validate()
  if (!validation.valid) return
  try {
    await store.login()
    if (store.isAuthenticated) {
      router.push({ name: 'Home' })
    }
  } catch (err) {
    console.error('Login failed', err)
  }
}

function onReset() {
  store.resetForm()
  if (formRef.value) {
    formRef.value.resetValidation()
  }
}
</script>

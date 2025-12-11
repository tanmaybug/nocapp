<template>
  <v-container>
    <v-card>
      <v-card-title class="text-center">Login</v-card-title>
      <v-card-text>
        <v-form ref="formRef" @submit.prevent="onSubmit">
          <v-row class="pa-2">
            <v-col cols="12">
              <v-text-field v-model="form.username" label="Username *" :rules="[requiredRule]" autocomplete="username" />
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="form.password" label="Password *" :rules="[requiredRule, passwordRule]" :type="showPassword ? 'text' : 'password'" :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'" @click:append-inner="showPassword = !showPassword" autocomplete="current-password" />
            </v-col>
            <v-col cols="12" class="d-flex justify-end">
              <v-btn variant="text" @click="onReset">Reset</v-btn>
              <v-btn class="ms-2" :disabled="false" @click="onSubmit">Login</v-btn>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { requiredRule, passwordRule } from '@/composables/validators'
import { useAuthStore } from '@/stores/authStore'
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'

const store = useAuthStore()
const { form } = storeToRefs(store)

const router = useRouter()

const formRef = ref<any>(null)
const showPassword = ref(false)

async function onSubmit() {
  const validation = await formRef.value.validate()
  if (!validation.valid) return
  await store.login()
  if (store.isAuthenticated) {
    router.push({ name: 'Home' })
  }
}

function onReset() {
  store.resetForm()
}
</script>

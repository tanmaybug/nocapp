<template>
  <div class="otp-input">
    <div class="otp-input__row">
      <v-text-field v-model="userInputValue" :readonly="isVerified" :type="userInputType" :label="userInputLabel" density="comfortable" :rules="userInputRules" :error-messages="userInputError ? [userInputError] : []" @keyup.enter.prevent="handleSend" @update:model-value="userInputError = ''" />
      <v-btn class="mb-5" :color="isVerified ? '#008080' : undefined" :prepend-icon="isVerified ? 'mdi-check-circle' : undefined" variant="outlined" :loading="sending && !showOTPDialog" :disabled="sending || !isContactValid || isVerified" @click="handleSend">
        {{ isVerified ? 'Verified' : sendButtonText }}
      </v-btn>
    </div>

    <v-dialog v-model="showOTPDialog" persistent max-width="420">
      <v-card>
        <v-card-text class="pt-5">
          <div class="text-body-2 mb-4 text-center">{{ dialogTitle }}</div>
          <v-otp-input :error="otpError" v-model="otpValue" focus-all :length="otpLength" :label="otpLabel" type="text" autofocus class="mt-2" />
          <v-divider class="mt-3 mb-6"></v-divider>

          <div class="mb-3 text-body-2">
            Need another <strong>code</strong>?
          </div>

          <v-btn color="primary" size="small" text="Resend" variant="outlined" :loading="sending && showOTPDialog" @click="handleSend"></v-btn>
        </v-card-text>

        <v-card-actions>
          <v-spacer />
          <v-btn variant="text" @click="handleCancel">Cancel</v-btn>
          <v-btn color="primary" variant="outlined" :disabled="!isOtpValid" @click="handleSubmitOtp">
            {{ verifyButtonText }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

type ValidationRule = (value: string) => true | string
type SendOtpHandler = (payload: { userInput: string }) => Promise<any>
type VerifyOtpHandler = (payload: { userInput: string, otp: string }) => Promise<any>

const userInputError = ref('')
const sending = ref(false)
const showOTPDialog = ref(false)
const otpError = ref(false)
const userInputValue = defineModel('userInputValue', { type: String })
const otpValue = defineModel('otpValue', { type: Number })
const isVerified = defineModel('isVerified', { type: Boolean, default: false })

const props = withDefaults(defineProps<{
  userInputLabel?: string
  userInputType?: string
  sendButtonText?: string
  otpLabel?: string
  otpLength?: number
  verifyButtonText?: string
  dialogTitle?: string
  sendOtp: SendOtpHandler
  verifyOtp: VerifyOtpHandler
  userInputRules?: ValidationRule[]
}>(), {
  userInputLabel: 'Mobile Number',
  userInputType: 'text',
  sendButtonText: 'Send OTP',
  otpLabel: 'Enter OTP',
  otpLength: 6,
  verifyButtonText: 'Verify OTP',
  dialogTitle: `Please enter the OTP`,
  userInputRules: () => [
    (value: string) => !!value || 'This field is required.',
  ],
})

const isOtpValid = computed(() => otpValue.value.trim().length === props.otpLength)
const isContactValid = computed(() => runContactValidation(userInputValue.value.trim()) === true)

async function handleSend() {
  const validationResult = runContactValidation(userInputValue.value.trim())
  if (validationResult !== true) {
    userInputError.value = validationResult
    return
  }

  try {
    sending.value = true
    await props.sendOtp({ userInput: userInputValue.value.trim() })
    otpValue.value = ''
    showOTPDialog.value = true
  } catch (error) {
    userInputError.value = 'Failed to send OTP.'
  } finally {
    sending.value = false
  }
}

async function handleSubmitOtp() {
  if (!isOtpValid.value) return

  try {
    await props.verifyOtp({ userInput: userInputValue.value.trim(), otp: otpValue.value.trim() })
    showOTPDialog.value = false
    otpError.value = false
    isVerified.value = true
  } catch (error) {
    otpError.value = true
  }
}

function handleCancel() {
  showOTPDialog.value = false
  otpError.value = false
  otpValue.value = ''
}

function runContactValidation(value: string): true | string {
  const rules = props.userInputRules || []
  for (const rule of rules) {
    const result = rule(value)
    if (result !== true) {
      return typeof result === 'string' ? result : 'Invalid value'
    }
  }
  return true
}
</script>

<style scoped>
.otp-input {
  width: 100%;
}

.otp-input__row {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

@media (min-width: 600px) {
  .otp-input__row {
    flex-direction: row;
    align-items: flex-start;
  }

  .otp-input__row .v-btn {
    align-self: center;
    min-width: 140px;
  }
}
</style>

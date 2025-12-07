export type NumericRuleMessages = {
  digits?: string
  length?: string | ((expectedLength: number) => string)
  min?: string | ((minValue: number) => string)
  max?: string | ((maxValue: number) => string)
}

export type NumericOptions = {
  length?: number
  min?: number
  max?: number
  allowDecimal?: boolean
  messages?: NumericRuleMessages
}

export const requiredRule = (v: any) => (!!v && (Array.isArray(v) ? v.length > 0 : true)) || 'This field is required'

export const emailRule = (v: any) => /\S+@\S+\.\S+/.test(String(v || '')) || 'Invalid email'

export const passwordRule = (v: any) => (String(v || '').length >= 6) || 'Password must be at least 6 characters'

export function makeMatchRule(getValue: () => any, message = 'Values do not match') {
  return (v: any) => v === getValue() || message
}

export function requiredIfRule(condition: boolean | (() => boolean), message = 'This field is required') {
  return (v: any) => {
    const active = typeof condition === 'function' ? (condition as () => boolean)() : condition
    if (!active) return true
    return (!!v && (Array.isArray(v) ? v.length > 0 : true)) || message
  }
}

function resolveMessage<T>(custom: string | ((arg: T) => string) | undefined, fallback: string | ((arg: T) => string), arg: T): string {
  if (custom !== undefined) {
    return typeof custom === 'function' ? custom(arg) : custom
  }
  return typeof fallback === 'function' ? fallback(arg) : fallback
}

export function numericRule(options: NumericOptions) {
  const defaultMessages = {
    digits: 'Must contain digits only',
    length: (len: number) => `Must be exactly ${len} digits`,
    min: (minVal: number) => `Must be >= ${minVal}`,
    max: (maxVal: number) => `Must be <= ${maxVal}`,
  }

  return (v: any) => {
    const s = String(v ?? '')
    if (!s) return true

    const allowDecimal = options.allowDecimal ?? false
    const pattern = allowDecimal ? /^[0-9]+(\.[0-9]+)?$/ : /^[0-9]+$/
    if (!pattern.test(s)) {
      return resolveMessage(options.messages?.digits, defaultMessages.digits, undefined as never)
    }

    if (options.length !== undefined) {
      return (
        s.length === options.length ||
        resolveMessage(options.messages?.length, defaultMessages.length, options.length)
      )
    }

    const n = Number(s)
    if (options.min !== undefined && n < options.min) {
      return resolveMessage(options.messages?.min, defaultMessages.min, options.min)
    }
    if (options.max !== undefined && n > options.max) {
      return resolveMessage(options.messages?.max, defaultMessages.max, options.max)
    }
    return true
  }
}

export function isNumericValidRule(value: any, options: NumericOptions) {
  const s = String(value || '')
  const allowDecimal = options.allowDecimal ?? false
  const pattern = allowDecimal ? /^[0-9]+(\.[0-9]+)?$/ : /^[0-9]+$/
  if (!pattern.test(s)) return false
  if (options.length !== undefined) return s.length === options.length
  const n = Number(s)
  if (options.min !== undefined && n < options.min) return false
  if (options.max !== undefined && n > options.max) return false
  return true
}

export const fileRequiredRule = (v: any) => {
  if (!v) return 'This field is required'
  if (Array.isArray(v)) return v.length > 0 || 'At least one file required'
  return true
}

export function alphanumericRule(length?: number) {
  return (v: any) => {
    const s = String(v || '')
    if (!s) return true // Optional field
    if (!/^[a-zA-Z0-9]+$/.test(s)) return 'Must contain only letters and numbers'
    if (length !== undefined && s.length !== length) return `Must be exactly ${length} characters`
    return true
  }
}

export const mobileRule = (v: any) => {
  const s = String(v || '')
  if (!/^[0-9]{10}$/.test(s)) return 'Must be a valid 10-digit mobile number'
  return true
}

export type NumericOptions = { length?: number; min?: number; max?: number }

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

export function numericRule(options: NumericOptions) {
  return (v: any) => {
    const s = String(v || '')
    if (!/^[0-9]+$/.test(s)) return 'Must contain digits only'
    if (options.length !== undefined) {
      return s.length === options.length || `Must be exactly ${options.length} digits`
    }
    const n = Number(s)
    if (options.min !== undefined && n < options.min) return `Must be >= ${options.min}`
    if (options.max !== undefined && n > options.max) return `Must be <= ${options.max}`
    return true
  }
}

export function isNumericValidRule(value: any, options: NumericOptions) {
  const s = String(value || '')
  if (!/^[0-9]+$/.test(s)) return false
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

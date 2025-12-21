import api from '@/services/api'

export const sendOtp = async (payload: { userInput: string }) => {
  const resp = await api.post(`/otp/getOTP`, payload)
  return resp.data
}

export const verifyOtp = async (payload: { userInput: string; otp: string }) => {
  const resp = await api.post(`/otp/otpVerification`, payload)
  return resp.data
}

export const submitLogin = async (payload: { username: string; password: string }) => {
  const resp = await api.post('/login', payload)
  return resp.data
}

export const getRegistrationFormOptions = async () => {
  const resp = await api.get('/registration')
  return resp.data
}

export const submitRegistration = async (payload: any) => {
  const resp = await api.post('/registration/submit', payload)
  return resp.data
}

export const getPostOffices = async (pin: number) => {
  const resp = await api.get(`/registration/postOffices/${pin}`)
  return resp.data
}

export const getGramPanchayats = async (municipalityBlockId: number) => {
  const resp = await api.get(`/registration/grampanchayats/${municipalityBlockId}`)
  return resp.data
}

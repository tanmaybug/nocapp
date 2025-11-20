import axios from 'axios'
import type { State, District, SubDivision } from '@/types/common'

const baseURL = import.meta.env.VITE_API_BASE_URL || ''

const api = axios.create({
  baseURL,
  headers: { 'Content-Type': 'application/json' },
})

export const getStates = async (): Promise<State[]> => {
  const resp = await api.get('/states')
  return resp.data as State[]
}

export const getDistricts = async (): Promise<District[]> => {
  const resp = await api.get('/districts')
  return resp.data as District[]
}

export const getSubdivisions = async (): Promise<SubDivision[]> => {
  const resp = await api.get('/subdivisions')
  return resp.data as SubDivision[]
}

export const createNocApplication = async (payload: any) => {
  const resp = await api.post('/noc-applications', payload)
  return resp.data
}

export const submitRegistration = async (payload: any) => {
  const resp = await api.post('/registration/submit', payload)
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

export const getPostOffices = async (pin: number) => {
  const resp = await api.get(`/registration/postOffices/${pin}`)
  return resp.data
}

export const getGramPanchayats = async (municipalityBlockId: number) => {
  const resp = await api.get(`/registration/grampanchayats/${municipalityBlockId}`)
  return resp.data
}

export default api

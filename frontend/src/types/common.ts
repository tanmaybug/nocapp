export type State = {
  id: string
  name: string
}

export type District = {
  id: string
  name: string
  stateId: string
}

export type SubDivision = {
  id: string
  name: string
  districtId: string
}

export const STATUS = {
  INITIALIZED: 'initialized', 
  PROCESSING: 'processing',
  PROCESSED: 'processed',
  FAILED: 'failed'
} as const

export type Status = typeof STATUS[keyof typeof STATUS]
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

export type Status = 'initialized' | 'processing' | 'processed' | 'failed'
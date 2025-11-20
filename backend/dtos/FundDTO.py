from pydantic import BaseModel
from typing import List

class FundUtilizationRequestDTO(BaseModel):
    year: str | None = None
    source: str | None = None
    utilisation: str | None = None

class FundUtilizationRequestDTOBatch(BaseModel):
    items: List[FundUtilizationRequestDTO]
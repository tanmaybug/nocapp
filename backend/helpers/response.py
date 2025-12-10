from pydantic import BaseModel
from typing import Any, Optional

class APIResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[Any] = None  # data is optional
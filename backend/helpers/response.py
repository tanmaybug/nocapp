from pydantic import BaseModel
from typing import Any

class APIResponse(BaseModel):
    status_code:int
    message:str
    data: Any
        
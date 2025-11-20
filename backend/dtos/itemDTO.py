from pydantic import BaseModel

class ItemResponseDTO(BaseModel):
    test_id: int
    sname: str
    phone: str
    email: str
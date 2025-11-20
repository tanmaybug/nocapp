from pydantic import BaseModel


class StudentResponseDTO(BaseModel):
    student_registration_no: str
    student_name: str
    phone: str
    email: str
    address:str

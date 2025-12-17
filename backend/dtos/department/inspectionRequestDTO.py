from pydantic import BaseModel

class SetInspectionRequest(BaseModel):
    nocRegId: str
    date: str

class InspectionFeedbackRequest(BaseModel):
    nocRegId: str
    remarks: str
    status: str
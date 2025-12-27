from pydantic import BaseModel

class ApplicationTrackResponse(BaseModel):
    sno: int
    activity: str
    date: int
    remarks: int
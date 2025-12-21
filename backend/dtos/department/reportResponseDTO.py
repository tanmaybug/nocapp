from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ApplicationListReport(BaseModel):
    registrationId: Optional[str]
    institutionName: Optional[str]
    applicantName: Optional[str]
    applicantPhone: Optional[int]
    applicantEmail: Optional[str]


class CollegeInfrastructure(BaseModel):
    ed_tech_labs: Optional[int]
    language_labs: Optional[int]
    conference_room: bool
    meeting_room: bool
    built_up_area_sqft: Optional[float]

class CollegeProfile(BaseModel):
    objective: Optional[str]
    experience: Optional[str]
    reputation: Optional[str]
    development_plan: Optional[str]
    funding_source: Optional[str]
    land_mouza: Optional[str]
    created_at: datetime
    infrastructure: CollegeInfrastructure

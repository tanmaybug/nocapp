from pydantic import BaseModel, Field, EmailStr, field_validator
from datetime import datetime
from typing import Literal
# import re

from utils.customValidation import phoneNumberValidation


class TestFormRequestDTO(BaseModel):
    name: str = Field(pattern="^[a-zA-Z]+$")
    phone_number: int
    email: EmailStr
    address: str | None = Field(default=None)  # Optional
    age: int | None
    subscription_status: Literal["Active", "Inactive"]
    create_time: datetime
    father_name: str = Field(pattern="^[a-zA-Z]+$")

    # class Config:
    #     orm_mode = True

    @field_validator("phone_number")
    def check_phone_number(cls, v):
        if not phoneNumberValidation(v):
            raise ValueError("Please Enter Valid Phone Number")
        
        return v

    # @field_validator("phone_number")
    # def check_phone_number(cls, v):
    #     pattern = r"^[6-9]\d{9}$"
    #     if not re.fullmatch(pattern, str(v)):
    #         raise ValueError("Please Enter Valid Phone Number")

    #     if len(str(v)) < 10:
    #         raise ValueError("Phone Number Must be 10 digits")

    #     return v

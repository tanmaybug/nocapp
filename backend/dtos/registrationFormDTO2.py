from pydantic import BaseModel, Field, field_validator, ValidationInfo
from datetime import date

from utils.customValidation import phoneNumberValidation


class RegistrationFormRequestDTO(BaseModel):
    applicant_type_id: int | None = Field(default=None)
    applicant_name: str = Field(pattern="^[A-Za-z. ]+$")
    applicant_mobile: int | None = Field(default=None)
    applicant_state_id: int | None = Field(default=None)
    applicant_dst_id: int | None = Field(default=None)
    applicant_subdiv_id: int | None = Field(default=None)
    applicant_block_id: int | None = Field(default=None)
    applicant_post_office_id: int | None = Field(default=None)
    applicant_pin: int | None = Field(default=None)
    applicant_mun_pan_id: int | None = Field(default=None)
    legal_entity_status: int | None = Field(default=None)
    societies_registration_act_id: int | None = Field(default=None)
    minority_flag: int | None = Field(default=None)
    registration_no: int | None = Field(default=None)
    registration_date: date | None = Field(default=None)
    registration_place: str | None = Field(default=None)
    applicant_qualification_id: int | None = Field(default=None)
    applicant_exp: int | None = Field(default=None)
    land_educational_purpose_flag: int | None = Field(default=None)
    land_owned_flag: int | None = Field(default=None)
    registration_acceptance_flag: int | None = Field(default=None)

    password:str
    confirm_password:str

    # class Config:
    #     orm_mode = True

    @field_validator("applicant_mobile")
    def check_phone_number(cls, v):
        if not phoneNumberValidation(v):
            raise ValueError("Please Enter Valid Phone Number")
        
        return v
    
    @field_validator("confirm_password")
    @classmethod
    def passwords_match(cls, v: str, info: ValidationInfo) -> str:
        if "password" in info.data and v != info.data["password"]:
            raise ValueError("Passwords do not match.")
        return v

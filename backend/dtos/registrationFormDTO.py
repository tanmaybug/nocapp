# from typing import List
from pydantic import BaseModel, Field, model_validator, ValidationError,ConfigDict

from utils.customValidation import (
    pinNumberValidation,
    phoneNumberValidation,
    emailValidation,
)


# class FinancialRow(BaseModel):
#     year: str | None = Field(pattern="^\d{4}$",default=None,description="Financial year (e.g., 2024,2025)")
#     source: str | None = Field(default=None, description="Source of funds")
#     utilisation: str | None = Field(default=None, description="Utilisation of funds")


class Applicantaddress(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    applicantAddress: str | None = Field(default=None, description="Address")
    districtId: int | None = Field(default=None, description="District ID")
    subDivisionId: int | None = Field(default=None, description="Subdivision ID")
    policeStationId: int | None = Field(default=None, description="Police station name")
    postOfficeId: int | None = Field(default=None, description="Post office name")
    municipalityBlockId: int | None = Field(default=None, description="Panchayat name")
    assemblyConstituencyId: int | None = Field(default=None, description="Assembly constituency")
    city: str | None = Field(default=None, description="City name")
    pin: int | None = Field(description="6-digit PIN code")

    
    @model_validator(mode="after")
    def check_pin_number(cls, values):
        error = []
        if not pinNumberValidation(values.pin):
            error.append(
                {
                    "type": "value_error",
                    "loc": ("pin",),
                    "msg": "Please Enter Valid PIN Number For Applicant Address",
                    "input": values.pin,
                    "ctx": {
                        "error": ValueError(
                            "Please Enter Valid PIN Number For Applicant Address"
                        )
                    },
                }
            )
        if error:
            raise ValidationError.from_exception_data(
                title="Validation error",
                line_errors=error,
            )
        return values

class Collegeaddress(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    college_address: str | None = Field(default=None, description="Address")
    districtId: int | None = Field(default=None, description="District ID")
    subDivisionId: int | None = Field(default=None, description="Subdivision ID")
    policeStationId: int | None = Field(default=None, description="Police station name")
    postOfficeId: int | None = Field(default=None, description="Post office name")
    gramPanchayatId: int | None = Field(default=None, description="Panchayat name")
    assemblyConstituencyId: int | None = Field(default=None, description="Assembly constituency")
    municipalityBlockId: int | None = Field(default=None, description="Block name")
    pin: int | None = Field(description="6-digit PIN code")

    @model_validator(mode="after")
    def check_pin_number(cls, values):
        error = []
        if not pinNumberValidation(values.pin):
            error.append(
                {
                    "type": "value_error",
                    "loc": ("pin",),
                    "msg": "Please Enter Valid PIN Number For College Address",
                    "input": values.pin,
                    "ctx": {
                        "error": ValueError(
                            "Please Enter Valid PIN Number For College Address"
                        )
                    },
                }
            )
        if error:
            raise ValidationError.from_exception_data(
                title="Validation error",
                line_errors=error,
            )
        return values


class RegistrationFormRequestDTO(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    
    entityTypeID: int | None = Field(default=None, description="Legal Entity Type")
    applicantName: str | None = Field(default=None, description="Applicant Name")
    isRegistered: int | None = Field(default=None, description="Legal Entity Status")
    minorityTypeId: int | None = Field(default=None, description="Minority Type")
    minorityFlag: int | None = Field(default=None, description="Minority Flag")
    registrationNo: str | None = Field(default=None, description="Registration Number")
    registrationDate: str | None = Field(default=None, description="Registration Date")
    placeOfRegistration: str | None = Field(default=None, description="Registration Place")
    minorityDetails: str | None = Field(default=None, description="Minority Status")

    applicantMobileNo: int | None = Field(default=None, description="Applicant Mobile Number")
    applicantEmailId: str | None = Field(default=None, description="Applicant Email Id")
    applicantTanNo: str | None = Field(default=None, description="Applicant TAN Number")
    
    applicantLocation: Applicantaddress = Field(description="Applicant Address details")
    
    proposedCollegeName: str | None = Field(
        default=None, description="Name of College Name"
    )
    affiliatedUniversityId: int | None = Field(
        default=None, description="Name of affiliating university"
    )
    institutionForId: int | None = Field(
        default=None, description="Institution purpose/type"
    )
    # financialRows: List[FinancialRow] = Field(description="List of financial rows")

    collegeLocation: Collegeaddress = Field(description="College Address details")

    """
    password pattern : ^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$
    
    Has minimum 8 characters in length.
    At least one uppercase letter.
    At least one lowercase letter.
    At least one digit.
    At least one special character.

    """
                         
    password: str = Field(description="Password")
    confirm_password: str = Field(description="Confirm Password")

    @model_validator(mode="after")
    def check_all(cls, values):
        errors = []

        if values.password != values.confirm_password:
            errors.append(
                {
                    "type": "value_error",
                    "loc": ("confirm_password",),
                    "msg": "Passwords do not match",
                    "input": values.confirm_password,
                    "ctx": {"error": ValueError("Passwords do not match")},
                }
            )

        if values.entityTypeID == 4 and values.minorityDetails == "":
            errors.append(
                {
                    "type": "value_error",
                    "loc": ("minorityDetails",),
                    "msg": "Please Enter Minority Details",
                    "input": values.minorityDetails,
                    "ctx": {"error": ValueError("Please Enter Minority Details")},
                }
            )

        if values.minorityFlag and values.minorityDetails == "":
            errors.append(
                {
                    "type": "value_error",
                    "loc": ("minorityDetails",),
                    "msg": "Please Enter Minority Details",
                    "input": values.minorityDetails,
                    "ctx": {"error": ValueError("Please Enter Minority Details")},
                }
            )

        if not phoneNumberValidation(values.applicantMobileNo):
            errors.append(
                {
                    "type": "value_error",
                    "loc": ("applicantMobileNo",),
                    "msg": "Please Enter Valid Phone Number",
                    "input": values.applicantMobileNo,
                    "ctx": {"error": ValueError("Please Enter Valid Phone Number")},
                }
            )

        if not emailValidation(values.applicantEmailId):
            errors.append(
                {
                    "type": "value_error",
                    "loc": ("applicantEmailId",),
                    "msg": "Please Enter Valid Email Id",
                    "input": values.applicantEmailId,
                    "ctx": {"error": ValueError("Please Enter Valid Email Id")},
                }
            )

        if errors:
            raise ValidationError.from_exception_data(
                title="Validation error",
                line_errors=errors,
            )

        return values
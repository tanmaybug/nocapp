from pydantic import BaseModel, Field, field_validator
from typing import Optional, Literal
from datetime import date


class BaseModelWithEmptyString(BaseModel):
    @field_validator("*", mode="before")
    def empty_string_to_none_and_trim(cls, v):
        # If the value is a string, trim it
        if isinstance(v, str):
            v = v.strip()
            # Convert empty string to None
            if v == "":
                return None
        return v


class ProjectedFundFlow(BaseModelWithEmptyString):
    amount: Optional[float] = Field(
        None, description="Amount (Numeric field, 10,2 precision)"
    )
    sourceOfFund: Optional[str] = Field(None, description="Source of Fund (Text field)")

    # @validator("amount")
    # def validate_amount_precision(cls, v):
    #     if v is not None and (v < 0 or round(v, 2) != v):
    #         raise ValueError("Amount must be non-negative and have up to 2 decimal places")
    #     return v


class Synopsis(BaseModelWithEmptyString):
    proposedInvestment: Optional[float] = Field(None, description="Proposed Investment")
    proposedEmployment: Optional[int] = Field(None, description="Proposed Employment")
    professionalCollegesCountWithin25Km: Optional[int] = Field(
        None, ge=0, description="Number of professional colleges within 25 km"
    )
    feederSchoolCountWithin15Km: Optional[int] = Field(
        None, ge=0, description="Number of feeder schools within 15 km"
    )

class Form2(BaseModelWithEmptyString):
    projectedFundFlow: Optional[ProjectedFundFlow]
    synopsis: Optional[Synopsis]

    buildingCompletionStatus: Optional[int] = Field(None, description="1 = Yes, 0 = No")
    buildingCompletionDate: Optional[date] = Field(
        None, description="Date of completion if building is completed")

    buildingCompletionExpectedDate: Optional[date] = Field(
        None, description="Expected date of completion if building not completed")

    buildingPlanAmountToBeDeposited: Optional[int] = Field(
        None,
        description=(
            "1 = 1,00,000 Fresh (urban/metro), "
            "2 = 50,000 Fresh (rural), "
            "3 = 50,000 Existing Gov-aided (urban/metro), "
            "4 = 25,000 Existing Gov-aided (rural)"
        ),
    )
    estimatedIncomeAndExpenditureForFirst5Years: Optional[str] = Field(
        None, description="Estimated income and expenditure for first 5 years"
    )
    initialFundInformation: Optional[str] = Field(None, description="Information about initial fund")
    nationalizedBank: Optional[str] = Field(None, description="Selected Nationalized Bank")

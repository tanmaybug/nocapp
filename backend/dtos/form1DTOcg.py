from pydantic import BaseModel,field_validator
from typing import Optional, Literal

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


class AimAndObjective(BaseModelWithEmptyString):
    vision: Optional[str]= None
    mission: Optional[str]= None
    coreValues: Optional[str]= None
    aims: Optional[str]= None
    objectiveConcernedInstitution: Optional[str]= None


class CollegeLandDetails(BaseModelWithEmptyString):
    mouza: Optional[str]= None
    jlNo: Optional[str]= None
    khatianNo: Optional[str]= None
    plotNo: Optional[str]= None
    areaClasification: Optional[int]= None


class CredibilityAndReadiness(BaseModelWithEmptyString):
    experienceInEducation: Optional[str]= None
    generalReputation: Optional[str]= None
    readinessToComplyWithRegulatoryNorms: Optional[str]= None


class AdditionalCommitmentsAndPlans(BaseModelWithEmptyString):
    studentReservation: Optional[int]= None
    employeeReservation: Optional[int]= None
    specialSkillDevelomentActivity: Optional[int]= None
    academicAuditingPlans: Optional[int]= None


class LandStatus(BaseModelWithEmptyString):
    landOwnedStatus: Optional[int]= None
    landConvertedForEducationalPurposeStatus: Optional[int]= None


class ApprovedPlanWith(BaseModelWithEmptyString):
    totalBuildUpArea: Optional[float]= None
    groundFloorArea: Optional[float]= None
    firstFloorArea: Optional[float]= None


class TotalNumberOf(BaseModelWithEmptyString):
    classRoomCount: Optional[int]= None
    seminarRoomCount: Optional[int]= None
    multipurposeHallCount: Optional[int]= None
    labResourceCenterCount: Optional[int]= None
    ictEduTechLabCount: Optional[int]= None
    languageLabCount: Optional[int]= None
    storeRoomCount: Optional[int]= None
    boysCommonRoomCount: Optional[int]= None
    girlsCommonRoomCount: Optional[int]= None
    boysToiletCount: Optional[int]= None
    girlsToiletCount: Optional[int]= None


class AnyOtherRoom(BaseModelWithEmptyString):
    conferrenceRoomStatus: Optional[int]= None
    meetingRoomStatus: Optional[int]= None


class LibraryDetails(BaseModelWithEmptyString):
    totalSpace: Optional[float]= None
    readingRoomCount: Optional[int]= None
    booksCount: Optional[int]= None
    journalPeriodicalCount: Optional[int]= None

   


class CampusDevelopmentPlan(BaseModelWithEmptyString):
    approvedPlanWith: Optional[ApprovedPlanWith]= None
    totalNumberOf: Optional[TotalNumberOf]= None
    anyOtherRoom: Optional[AnyOtherRoom]= None
    libraryDetails: Optional[LibraryDetails]= None
    administrativeOfficeStatus: Optional[int]= None
    totalPlannedConstruction: Optional[float]= None


class Form1(BaseModelWithEmptyString):
    aimAndObjective: Optional[AimAndObjective]= None
    collegeLandDetails: Optional[CollegeLandDetails]= None
    credibilityAndReadiness: Optional[CredibilityAndReadiness]= None
    additionalCommitmentsAndPlans: Optional[AdditionalCommitmentsAndPlans]= None
    campusDevlopmentPlan: Optional[CampusDevelopmentPlan]= None
    comprehensivePlan: Optional[str]= None
    collegeLandAreaInAcres: Optional[float]= None
    collegeCoveredArea: Optional[float]= None
    landStatus: Optional[LandStatus]= None

    

    # @model_validator(mode="after")
    
    # def validate_land_area(cls, values):
    #     """Conditional validation for land area based on area classification."""
    #     area = values.get("collegeLandAreaInAcres")
    #     land_details = values.get("collegeLandDetails")
    #     if area is not None and land_details is not None:
    #         classification = land_details.areaClasification
    #         if classification == 1 and area < 3:
    #             raise ValueError("Urban area must be at least 3 acres.")
    #         if classification == 2 and area < 5:
    #             raise ValueError("Rural area must be at least 5 acres.")
    #     return values

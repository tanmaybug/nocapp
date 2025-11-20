from pydantic import BaseModel
from typing import Optional, Literal


class AimAndObjective(BaseModel):
    vision: Optional[str]
    mission: Optional[str]
    coreValues: Optional[str]
    aims: Optional[str]
    objectiveConcernedInstitution: Optional[str]


class CollegeLandDetails(BaseModel):
    mouza: Optional[str]
    jlNo: Optional[str]
    khatianNo: Optional[str]
    plotNo: Optional[str]
    areaClasification: Optional[int]


class CredibilityAndReadiness(BaseModel):
    experienceInEducation: Optional[str]
    generalReputation: Optional[str]
    readinessToComplyWithRegulatoryNorms: Optional[str]


class AdditionalCommitmentsAndPlans(BaseModel):
    studentReservation: Optional[int]
    employeeReservation: Optional[int]
    specialSkillDevelomentActivity: Optional[int]
    academicAuditingPlans: Optional[int]


class LandStatus(BaseModel):
    landOwnedStatus: Optional[int]
    landConvertedForEducationalPurposeStatus: Optional[int]


class ApprovedPlanWith(BaseModel):
    totalBuildUpArea: Optional[float]
    groundFloorArea: Optional[float]
    firstFloorArea: Optional[float]


class TotalNumberOf(BaseModel):
    classRoomCount: Optional[int]
    seminarRoomCount: Optional[int]
    multipurposeHallCount: Optional[int]
    labResourceCenterCount: Optional[int]
    ictEduTechLabCount: Optional[int]
    languageLabCount: Optional[int]
    storeRoomCount: Optional[int]
    boysCommonRoomCount: Optional[int]
    girlsCommonRoomCount: Optional[int]
    boysToiletCount: Optional[int]
    girlsToiletCount: Optional[int]


class AnyOtherRoom(BaseModel):
    conferrenceRoomStatus: Optional[int]
    meetingRoomStatus: Optional[int]


class LibraryDetails(BaseModel):
    totalSpace: Optional[float]
    readingRoomCount: Optional[int]
    booksCount: Optional[int]
    journalPeriodicalCount: Optional[int]


class CampusDevelopmentPlan(BaseModel):
    approvedPlanWith: Optional[ApprovedPlanWith]
    totalNumberOf: Optional[TotalNumberOf]
    anyOtherRoom: Optional[AnyOtherRoom]
    libraryDetails: Optional[LibraryDetails]
    administrativeOfficeStatus: Optional[int]
    totalPlannedConstruction: Optional[float]


class Form1(BaseModel):
    aimAndObjective: Optional[AimAndObjective]
    collegeLandDetails: Optional[CollegeLandDetails]
    credibilityAndReadiness: Optional[CredibilityAndReadiness]
    additionalCommitmentsAndPlans: Optional[AdditionalCommitmentsAndPlans]
    campusDevlopmentPlan: Optional[CampusDevelopmentPlan]
    comprehensivePlan: Optional[str]
    collegeLandAreaInAcres: Optional[float]
    collegeCoveredArea: Optional[float]
    landStatus: Optional[LandStatus]

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

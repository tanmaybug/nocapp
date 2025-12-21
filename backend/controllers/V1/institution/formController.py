from fastapi import APIRouter, HTTPException, status, Depends

# from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from config.DB.DBConfig import get_db
from helpers import response
# from services.form1Repo import form1Service
# from core.Dependencies.auth import get_current_user

router = APIRouter(prefix="/institution/form", tags=["Form"])


@router.get("", response_model=response.APIResponse)
def get_noc_application(
    db: Session = Depends(get_db),  # current_user: dict = Depends(get_current_user)
):
    # nocRegId = current_user["stake_user"]
    # result = form1Service(db).get_application_by_reg_id(nocRegId)

    # if not result:
    #     raise HTTPException(status_code=404, detail="Application not found")

    data = [
        {
            "form": {
                "form1": {
                    "aimAndObjective": {
                        "vision": "",
                        "mission": "",
                        "coreValues": "",
                        "aims": "",
                        "objectiveConcernedInstitution": "",
                    },
                    "collegeLandDetails": {
                        "mouza": "",
                        "jlNo": "",
                        "khatianType": "",
                        "khatianNo": "",
                        "plotType": "",
                        "plotNo": "",
                        "areaClasification": "",
                    },
                    "collegeLandAreaInAcres": "",
                    "collegeCoveredArea": "",
                    "credibilityAndReadiness": {
                        "experienceInEducation": "",
                        "generalReputation": "",
                        "readinessToComplyWithRegulatoryNorms": "",
                    },
                    "additionalCommitmentsAndPlans": {
                        "studentReservation": "",
                        "studentReservationDetails": "",
                        "employeeReservation": "",
                        "employeeReservationDetails": "",
                        "specialSkillDevelomentActivity": "",
                        "specialSkilDetails": "",
                        "academicAuditingPlans": "",
                        "academicAuditDetails": "",
                    },
                    "landStatus": {"landOwnedStatus": ""},
                    "comprehensivePlan": "",
                    "campusDevlopmentPlan": {
                        "approvedPlanWith": {
                            "totalBuildUpArea": "",
                            "groundFloorArea": "",
                            "firstFloorArea": "",
                        },
                        "totalNumberOf": {
                            "classRoomCount": "",
                            "seminarRoomCount": "",
                            "multipurposeHallCount": "",
                            "labResourceCenterCount": "",
                            "ictEduTechLabCount": "",
                            "languageLabCount": "",
                            "storeRoomCount": "",
                            "boysCommonRoomCount": "",
                            "girlsCommonRoomCount": "",
                            "boysToiletCount": "",
                            "girlsToiletCount": "",
                        },
                        "anyOtherRoom": {
                            "conferrenceRoomStatus": "",
                            "meetingRoomStatus": "",
                        },
                        "libraryDetails": {
                            "totalSpace": "",
                            "readingRoomCount": "",
                            "booksCount": "",
                            "journalPeriodicalCount": "",
                        },
                        "administrativeOfficeStatus": "",
                        "totalPlannedConstruction": "",
                    },
                },
                "form2": {
                    "projectedFundFlow": {"amount": "", "sourceOfFund": ""},
                    "synopsis": {
                        "proposedInvestment": "",
                        "proposedEmployment": "",
                        "professionalCollegesCountWithin25Km": "",
                        "feederSchoolCountWithin15Km": "",
                    },
                    "buildingCompletionStatus": "",
                    "buildingCompletionDate": "",
                    "buildingCompletionExpectedDate": "",
                    "buildingPlanAmountToBeDeposited": "",
                    "estimatedIncomeAndExpenditureForFirst5Years": "",
                    "initialFundInformation": "",
                    "nationalizedBank": "",
                },
                "form3": {
                    "proposalForCampusDevelopmentProgram": [],
                    "experienceAndExpertiseInDiscipline": [],
                    "feeStructureProposal": [],
                    "endowmentFundDetails": [],
                    "employeeAppointmentProcedure": [],
                    "extracurricularActivitiesAndPlacesDetails": [],
                    "societyRegistrationCertificate": [],
                    "conveyanceDeed": [],
                    "gripsEchallan": [],
                    "buildingPlan": [],
                    "proofoFFees": [],
                    "proofOfLand": [],
                    "phasedDevlopmentBluePrint": [],
                    "prrofOfContiguousLandOwnership": [],
                    "otherInformation": [],
                },
            },
            "submissionProgress": {"form1": False, "form2": False, "form3": False},
        }
    ]

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Form1 Updated Successfully",
        "data": data,
    }

    return result

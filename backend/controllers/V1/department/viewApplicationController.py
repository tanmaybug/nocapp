from fastapi import APIRouter, status, Depends, HTTPException
from helpers import response
from core.Dependencies.auth import get_current_admin
from fastapi.templating import Jinja2Templates
from xhtml2pdf import pisa  # type: ignore
import io
from pathlib import Path
from config.DB.DBConfig import get_db
# from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
from services.department.applicationRepo import applicationService

router = APIRouter(
    prefix="/department/ViewApplication", tags=["View Application"]
)

templates = Jinja2Templates(directory="templates")

@router.get("", response_model=response.APIResponse)
def get_application_data(
    nocRegId: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_admin),
):
    # print(current_user)
    # print(nocRegId)
    # userId = current_user["stake_user"]

    application_db_data = applicationService(db).get_application_data_by_id(nocRegId)
    if not application_db_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Record not found"
        )

    BASE_DIR = Path(__file__).resolve().parents[4]

    logo_path = BASE_DIR / "templates/static/images/Emblem_of_India.png"
    # logo_path = os.path.join(BASE_DIR, "templates/static/images/Emblem_of_India.png")

    data = {
        "applicantDetails": {
            "entityType": "Society",
            "applicantName": "Tanmay",
            "isMinority": "YES",
            "minorityType": "Linguistic",
            "language": "SANTALI",
            "religion": "",
            "applicationId": nocRegId,
            "applicantMobileNo": 9876543210,
            "applicantEmailId": "tanmay.sharma@email.com",
            "applicantTanNo": "TAN9876543",
            "applicantLocation": {
                "applicantAddress": "123, XYZ Street, Sector 15",
                "district": "Howrah",
                "subDivision": "Howrah Sub",
                "policeStation": "Bantra",
                "postOffice": "Kadamtala",
                "municipalityBlock": "Howrah",
                "city": "Gurgaon",
                "pin": 711101,
            },
        },
        "collegeDetails": {
            "proposedCollegeName": "Shree Ram College of Engineering",
            "affiliatedUniversity": "CU",
            "institutionFor": "Male",
            "collegeLocation": {
                "collegeAddress": "456, College Road, Sector 21",
                "districtId": "Howrah",
                "subDivisionId": "Howrah Sub",
                "policeStation": "Bantra",
                "postOffice": "Kadamtala",
                "gramPanchayat": "XYZ",
                "municipalityBlock": "XYZ Block",
                "pin": 711101,
            },
        },
        "institutionPurpose": {
            "aimAndObjective": {
                "vision": "To be a premier institution promoting innovation and excellence in engineering education.",
                "mission": "To provide world-class education, foster innovation, and create socially responsible engineers.",
                "coreValues": "Integrity, Excellence, Innovation, Inclusivity, Sustainability",
                "aims": "To provide a platform for young minds to achieve academic and personal growth, contributing to societal welfare.",
                "objectiveConcernedInstitution": "To meet the growing demand for skilled engineers by offering state-of-the-art learning resources.",
            },
            "collegeLandDetails": {
                "mouza": "Mauza-A",
                "jlNo": "156",
                "khatianNo": "1212",
                "plotNo": "99/7B",
                "areaClasification": 1,
            },
            "credibilityAndReadiness": {
                "experienceInEducation": "The trust has over 20 years of experience in running schools and training centers.",
                "generalReputation": "Recognized for its commitment to quality and community service in the region.",
                "readinessToComplyWithRegulatoryNorms": "Fully committed to complying with regulatory norms set by the government and affiliating body.",
            },
            "additionalCommitmentsAndPlans": {
                "studentReservation": 1,
                "employeeReservation": 1,
                "specialSkillDevelopmentActivity": 1,
                "academicAuditingPlans": 1,
            },
        },
        "campusDevelopment": {
            "campusDevlopmentPlan": {
                "approvedPlanWith": {
                    "totalBuildUpArea": 30000,
                    "groundFloorArea": 10000,
                    "firstFloorArea": 9000,
                },
                "totalNumberOf": {
                    "classRoomCount": 30,
                    "seminarRoomCount": 3,
                    "multipurposeHallCount": 1,
                    "labResourceCenterCount": 5,
                    "ictEduTechLabCount": 3,
                    "languageLabCount": 1,
                    "storeRoomCount": 2,
                    "boysCommonRoomCount": 1,
                    "girlsCommonRoomCount": 1,
                    "boysToiletCount": 6,
                    "girlsToiletCount": 6,
                },
                "anyOtherRoom": {"conferrenceRoomStatus": 1, "meetingRoomStatus": 1},
                "libraryDetails": {
                    "totalSpace": 2500,
                    "readingRoomCount": 3,
                    "booksCount": 15000,
                    "journalPeriodicalCount": 50,
                },
                "administrativeOfficeStatus": 1,
                "totalPlannedConstruction": 40000,
            },
            "comprehensivePlan": "In the next 5 years, we will expand the infrastructure, including hostels and recreational facilities.",
            "collegeLandAreaInAcres": 10.0,
            "collegeCoveredArea": 4.0,
            "landStatus": {
                "landOwnedStatus": 1,
                "landConvertedForEducationalPurposeStatus": 1,
            },
        },
        "financialDetails": {
            "projectedFundFlow": {
                "amount": "20000.5",
                "sourceOfFund": "Bank Loan, Trust Funds, Government Grants",
            },
            "synopsis": {
                "proposedInvestment": "15000.0",
                "proposedEmployment": "200",
                "professionalCollegesCountWithin25Km": "5",
                "feederSchoolCountWithin15Km": "10",
            },
            "buildingCompletionStatus": "Under Construction",
            "buildingCompletionDate": "2024-06-30",
            "buildingCompletionExpectedDate": "2026-12-31",
            "buildingPlanAmountToBeDeposited": "5000.0",
            "estimatedIncomeAndExpenditureForFirst5Years": "Projected income of 100000, projected expenditure of 80000",
            "initialFundInformation": "Initial capital from trust and government subsidy.",
            "nationalizedBank": "State Bank of India",
        },
        "documentData": {
            "proposalForCampusDevelopmentProgram": "https://example.com/campus-development-proposal",
            "experienceAndExpertiseInDiscipline": "https://example.com/experience-details",
            "feeStructureProposal": "https://example.com/fee-structure",
            "endowmentFundDetails": "https://example.com/endowment-fund",
            "employeeAppointmentProcedure": "https://example.com/employee-appointment",
            "extracurricularActivitiesAndPlacesDetails": "https://example.com/extracurricular-activities",
            "societyRegistrationCertificate": "https://example.com/society-registration",
            "conveyanceDeed": "https://example.com/conveyance-deed",
            "homesteadPurposeConversionApplication": "https://example.com/homestead-conversion",
            "gripsEchallan": "https://example.com/grips-echallan",
            "buildingPlan": "https://example.com/building-plan",
            "proofOfFees": "https://example.com/proof-of-fees",
            "proofOfLand": "https://example.com/proof-of-land",
            "phasedDevelopmentBluePrint": "https://example.com/phased-development",
            "proofOfContiguousLandOwnership": "https://example.com/land-ownership",
            "otherInformation": "https://example.com/other-information",
            "vision": "https://example.com/other-information",
            "mission": "https://example.com/other-information",
            "CoreValues": "https://example.com/other-information",
            "aims": "https://example.com/other-information",
            "objectivesOfGovernmentInstitution": "https://example.com/other-information",
            "khatian": "https://example.com/other-information",
            "totalAreaOfLandForCollege": "https://example.com/other-information",
            "applicationFeesToBeDepositedToHED": "https://example.com/other-information",
        },
        "logoPath": logo_path,
    }
    # Render the template with the request context (mandatory in FastAPI for Jinja2)
    html_content = templates.get_template("applicant_noc_profile_view.html").render(**data)
    return html_content


@router.get("/download")
def download_application(
    nocRegId: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_admin),
):
    application_db_data = applicationService(db).get_application_data_by_id(nocRegId)
    if not application_db_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Record not found"
        )

    BASE_DIR = Path(__file__).resolve().parents[4]

    logo_path = BASE_DIR / "templates/static/images/Emblem_of_India.png"
    data = {
        "applicantDetails": {
            "entityType": "Society",
            "applicantName": "Tanmay",
            "isMinority": "YES",
            "minorityType": "Linguistic",
            "language": "SANTALI",
            "religion": "",
            "applicationId": nocRegId,
            "applicantMobileNo": 9876543210,
            "applicantEmailId": "tanmay.sharma@email.com",
            "applicantTanNo": "TAN9876543",
            "applicantLocation": {
                "applicantAddress": "123, XYZ Street, Sector 15",
                "district": "Howrah",
                "subDivision": "Howrah Sub",
                "policeStation": "Bantra",
                "postOffice": "Kadamtala",
                "municipalityBlock": "Howrah",
                "city": "Gurgaon",
                "pin": 711101,
            },
        },
        "collegeDetails": {
            "proposedCollegeName": "Shree Ram College of Engineering",
            "affiliatedUniversity": "CU",
            "institutionFor": "Male",
            "collegeLocation": {
                "collegeAddress": "456, College Road, Sector 21",
                "districtId": "Howrah",
                "subDivisionId": "Howrah Sub",
                "policeStation": "Bantra",
                "postOffice": "Kadamtala",
                "gramPanchayat": "XYZ",
                "municipalityBlock": "XYZ Block",
                "pin": 711101,
            },
        },
        "institutionPurpose": {
            "aimAndObjective": {
                "vision": "To be a premier institution promoting innovation and excellence in engineering education.",
                "mission": "To provide world-class education, foster innovation, and create socially responsible engineers.",
                "coreValues": "Integrity, Excellence, Innovation, Inclusivity, Sustainability",
                "aims": "To provide a platform for young minds to achieve academic and personal growth, contributing to societal welfare.",
                "objectiveConcernedInstitution": "To meet the growing demand for skilled engineers by offering state-of-the-art learning resources.",
            },
            "collegeLandDetails": {
                "mouza": "Mauza-A",
                "jlNo": "156",
                "khatianNo": "1212",
                "plotNo": "99/7B",
                "areaClasification": 1,
            },
            "credibilityAndReadiness": {
                "experienceInEducation": "The trust has over 20 years of experience in running schools and training centers.",
                "generalReputation": "Recognized for its commitment to quality and community service in the region.",
                "readinessToComplyWithRegulatoryNorms": "Fully committed to complying with regulatory norms set by the government and affiliating body.",
            },
            "additionalCommitmentsAndPlans": {
                "studentReservation": 1,
                "employeeReservation": 1,
                "specialSkillDevelopmentActivity": 1,
                "academicAuditingPlans": 1,
            },
        },
        "campusDevelopment": {
            "campusDevlopmentPlan": {
                "approvedPlanWith": {
                    "totalBuildUpArea": 30000,
                    "groundFloorArea": 10000,
                    "firstFloorArea": 9000,
                },
                "totalNumberOf": {
                    "classRoomCount": 30,
                    "seminarRoomCount": 3,
                    "multipurposeHallCount": 1,
                    "labResourceCenterCount": 5,
                    "ictEduTechLabCount": 3,
                    "languageLabCount": 1,
                    "storeRoomCount": 2,
                    "boysCommonRoomCount": 1,
                    "girlsCommonRoomCount": 1,
                    "boysToiletCount": 6,
                    "girlsToiletCount": 6,
                },
                "anyOtherRoom": {"conferrenceRoomStatus": 1, "meetingRoomStatus": 1},
                "libraryDetails": {
                    "totalSpace": 2500,
                    "readingRoomCount": 3,
                    "booksCount": 15000,
                    "journalPeriodicalCount": 50,
                },
                "administrativeOfficeStatus": 1,
                "totalPlannedConstruction": 40000,
            },
            "comprehensivePlan": "In the next 5 years, we will expand the infrastructure, including hostels and recreational facilities.",
            "collegeLandAreaInAcres": 10.0,
            "collegeCoveredArea": 4.0,
            "landStatus": {
                "landOwnedStatus": 1,
                "landConvertedForEducationalPurposeStatus": 1,
            },
        },
        "financialDetails": {
            "projectedFundFlow": {
                "amount": "20000.5",
                "sourceOfFund": "Bank Loan, Trust Funds, Government Grants",
            },
            "synopsis": {
                "proposedInvestment": "15000.0",
                "proposedEmployment": "200",
                "professionalCollegesCountWithin25Km": "5",
                "feederSchoolCountWithin15Km": "10",
            },
            "buildingCompletionStatus": "Under Construction",
            "buildingCompletionDate": "2024-06-30",
            "buildingCompletionExpectedDate": "2026-12-31",
            "buildingPlanAmountToBeDeposited": "5000.0",
            "estimatedIncomeAndExpenditureForFirst5Years": "Projected income of 100000, projected expenditure of 80000",
            "initialFundInformation": "Initial capital from trust and government subsidy.",
            "nationalizedBank": "State Bank of India",
        },
        "documentData": {
            "proposalForCampusDevelopmentProgram": "https://example.com/campus-development-proposal",
            "experienceAndExpertiseInDiscipline": "https://example.com/experience-details",
            "feeStructureProposal": "https://example.com/fee-structure",
            "endowmentFundDetails": "https://example.com/endowment-fund",
            "employeeAppointmentProcedure": "https://example.com/employee-appointment",
            "extracurricularActivitiesAndPlacesDetails": "https://example.com/extracurricular-activities",
            "societyRegistrationCertificate": "https://example.com/society-registration",
            "conveyanceDeed": "https://example.com/conveyance-deed",
            "homesteadPurposeConversionApplication": "https://example.com/homestead-conversion",
            "gripsEchallan": "https://example.com/grips-echallan",
            "buildingPlan": "https://example.com/building-plan",
            "proofOfFees": "https://example.com/proof-of-fees",
            "proofOfLand": "https://example.com/proof-of-land",
            "phasedDevelopmentBluePrint": "https://example.com/phased-development",
            "proofOfContiguousLandOwnership": "https://example.com/land-ownership",
            "otherInformation": "https://example.com/other-information",
            "vision": "https://example.com/other-information",
            "mission": "https://example.com/other-information",
            "CoreValues": "https://example.com/other-information",
            "aims": "https://example.com/other-information",
            "objectivesOfGovernmentInstitution": "https://example.com/other-information",
            "khatian": "https://example.com/other-information",
            "totalAreaOfLandForCollege": "https://example.com/other-information",
            "applicationFeesToBeDepositedToHED": "https://example.com/other-information",
        },
        "logoPath": logo_path,
    }
    # Render HTML
    html_content = templates.get_template("applicant_noc_profile_view_pdf.html").render(
        **data
    )
    pdf = convert_html_to_pdf(html_content)

    return StreamingResponse(
        io.BytesIO(pdf),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=NOC_Application.pdf"},
    )

def convert_html_to_pdf(source_html: str):
    output = io.BytesIO()
    pisa_status = pisa.CreatePDF(io.StringIO(source_html), dest=output)
    if pisa_status.err:
        return None
    return output.getvalue()
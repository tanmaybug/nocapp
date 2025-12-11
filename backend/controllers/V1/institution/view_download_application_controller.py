from fastapi import APIRouter, status, Depends, Request
from helpers import response

from fastapi.responses import StreamingResponse
# from jinja2 import Environment, FileSystemLoader
from fastapi.templating import Jinja2Templates

# from weasyprint import HTML
from xhtml2pdf import pisa
import io
from core.Dependencies.auth import get_current_user
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/institution/NOCApplication", tags=["NOCApplication"])
# Setup Jinja2 environment
# templates = Environment(loader=FileSystemLoader("templates"))
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def view_application(request: Request):
    # Render the template with the request context (mandatory in FastAPI for Jinja2)
    html_content = templates.TemplateResponse(
        "applicant_noc_profile_view.html", {"request": request}
    )
    return html_content

@router.get("/")
def view_application_old(
    current_user: dict = Depends(get_current_user),
):
    nocRegId = current_user["stake_user"]
    data = {
        "applicantDetails": {
            "entityType": "Society",
            "applicantName": "Tanmay",
            "isRegistered": "YES",
            "minorityType": "YES",
            "minorityFlag": "YES",
            "registrationNo": nocRegId,
            "registrationDate": "2022-05-12",
            "placeOfRegistration": "New Delhi",
            "minorityDetails": "Muslim",
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
                "assemblyConstituency": "Shibpur",
                "city": "Gurgaon",
                "pin": 711101,
            },
        },
        "collegeDetails": {
            "proposedCollegeName": "Shree Ram College of Engineering",
            "affiliatedUniversity": "CU",
            "institutionFor": "XYZ",
            "collegeLocation": {
                "college_address": "456, College Road, Sector 21",
                "districtId": "Howrah",
                "subDivisionId": "Howrah Sub",
                "policeStation": "Bantra",
                "postOffice": "Kadamtala",
                "gramPanchayat": "XYZ",
                "assemblyConstituency": "Shibpur",
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
            "proposalForCampusDevelopmentProgram": [
                {"id": 1, "url": "https://example.com/campus-development-proposal"}
            ],
            "experienceAndExpertiseInDiscipline": [
                {"id": 2, "url": "https://example.com/experience-details"}
            ],
            "feeStructureProposal": [
                {"id": 3, "url": "https://example.com/fee-structure"}
            ],
            "endowmentFundDetails": [
                {"id": 4, "url": "https://example.com/endowment-fund"}
            ],
            "employeeAppointmentProcedure": [
                {"id": 5, "url": "https://example.com/employee-appointment"}
            ],
            "extracurricularActivitiesAndPlacesDetails": [
                {"id": 6, "url": "https://example.com/extracurricular-activities"}
            ],
            "societyRegistrationCertificate": [
                {"id": 7, "url": "https://example.com/society-registration"}
            ],
            "conveyanceDeed": [{"id": 8, "url": "https://example.com/conveyance-deed"}],
            "homesteadPurposeConversionApplication": [
                {"id": 9, "url": "https://example.com/homestead-conversion"}
            ],
            "gripsEchallan": [{"id": 10, "url": "https://example.com/grips-echallan"}],
            "buildingPlan": [{"id": 11, "url": "https://example.com/building-plan"}],
            "proofOfFees": [{"id": 12, "url": "https://example.com/proof-of-fees"}],
            "proofOfLand": [{"id": 13, "url": "https://example.com/proof-of-land"}],
            "phasedDevelopmentBluePrint": [
                {"id": 14, "url": "https://example.com/phased-development"}
            ],
            "proofOfContiguousLandOwnership": [
                {"id": 15, "url": "https://example.com/land-ownership"}
            ],
            "otherInformation": [
                {"id": 16, "url": "https://example.com/other-information"}
            ],
        },
    }

    result = response.APIResponse(
        status_code=status.HTTP_200_OK, message="NOC Application View", data=data
    )
    return result

@router.get("/download")
def download_application(
    request: Request,
    # current_user: dict = Depends(get_current_user),
):
    # data = {
    #     "invoice_number": "INV-001",
    #     "items": [
    #         {"name": "Laptop", "qty": 1, "price": 800},
    #         {"name": "Mouse", "qty": 2, "price": 25},
    #         {"name": "Keyboard", "qty": 1, "price": 50},
    #     ],
    # }

    # Render HTML
    html_content = templates.get_template("applicant_noc_profile_view.html").render({"request": request})

    # Ensure html_content is a string
    if isinstance(html_content, list):
        html_content = "".join(html_content)

    # template = templates.get_template("applicant_noc_profile_view.html")
    # html_content = template.render(**data)

    pdf = convert_html_to_pdf(html_content)

    return StreamingResponse(
        io.BytesIO(pdf),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=NOC_Application.pdf"},
    )
def convert_html_to_pdf(source_html: str):
    # Convert HTML string to PDF using WeasyPrint
    pdf = HTML(string=source_html).write_pdf()
    return pdf

def convert_html_to_pdf2(source_html: str):
    output = io.BytesIO()
    pisa_status = pisa.CreatePDF(io.StringIO(source_html), dest=output)
    if pisa_status.err:
        return None
    return output.getvalue()
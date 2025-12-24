from fastapi import APIRouter, status, Depends
from helpers import response
from core.Dependencies.auth import get_current_user

router = APIRouter(prefix="/institution/Dashboard", tags=["Dashboard"])


@router.get("", response_model=response.APIResponse)
def get_dashboard_data(current_user: dict = Depends(get_current_user)):
    print(current_user)
    # nocRegId = current_user["stake_user"]

    data = {
        "currentStatus": "SUBMITTED",
        "lastUpdatedDate": "12-10-2025",
        "isNOCCompleted": False,
        "activities": [
            {
                "sno": 1,
                "activity": "Registration",
                "date": "12-10-2025",
                "status": "COMPLETED",
            },
            {
                "sno": 2,
                "activity": "Form-1",
                "date": "12-10-2025",
                "status": "COMPLETED",
            },
            {"sno": 3, "activity": "Form-2", "date": "", "status": "PENDING"},
            {"sno": 4, "activity": "Form-3", "date": "", "status": "PENDING"},
            {
                "sno": 5,
                "activity": "Final Submition",
                "date": "",
                "status": "PENDING",
            },
            {
                "sno": 6,
                "activity": "Docket Number Added",
                "date": "",
                "status": "PENDING",
            },
        ],
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Dashbord Data",
        "data": data,
    }
    return result

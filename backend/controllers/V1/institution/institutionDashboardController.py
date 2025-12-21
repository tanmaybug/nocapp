from fastapi import APIRouter, status, Depends
from helpers import response
from core.Dependencies.auth import get_current_user

router = APIRouter(prefix="/institution/Dashboard", tags=["Dashboard"])


@router.get("", response_model=response.APIResponse)
def get_dashboard_data(current_user: dict = Depends(get_current_user)):
    print(current_user)
    # nocRegId = current_user["stake_user"]

    data = {
        "currentStatus": "Sumitted",
        "lastUpdatedDate": "12-10-2025",
        "isNOCCompleted": False,
        "trackData": [
            {"object": "Registration Done", "date": "12-10-2025", "status": "Done"},
            {"object": "Form-1", "date": "12-10-2025", "status": "Done"},
            {"object": "Form-2", "date": "12-10-2025", "status": "Pending"},
            {"object": "Form-3", "date": "12-10-2025", "status": "Pending"},
            {"object": "Final Submit Done", "date": "14-10-2025", "status": "Pending"},
            {
                "object": "Docket Number Added",
                "date": "20-10-2025",
                "status": "Pending",
            },
        ],
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Dashbord Data",
        "data": data,
    }
    return result

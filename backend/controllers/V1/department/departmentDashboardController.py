from fastapi import APIRouter, status, Depends
from helpers import response
from core.Dependencies.auth import get_current_admin

router = APIRouter(prefix="/department/Dashboard", tags=["Dashboard"])

@router.get("", response_model=response.APIResponse)
def get_dashboard_data(current_user: dict = Depends(get_current_admin)):
    
    print(current_user)
    # userId = current_user["stake_user"]

    data = {
        "totalPendingApplication": 10,
        "totalInProcessApplication":20,
        "totalNocCompleteApplication":30,
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Department Dashboard Data",
        "data": data,
    }
    return result
from fastapi import APIRouter, status, Depends
from helpers import response
from core.Dependencies.auth import get_current_admin

router = APIRouter(
    prefix="/department/InprocessApplication", tags=["Inprocess Application"]
)

@router.get("", response_model=response.APIResponse)
def get_application_data(current_user: dict = Depends(get_current_admin)):
    print(current_user)
    # userId = current_user["stake_user"]

    data = {
        "inprocessData": [
            {
                "name": "Test Inst",
                "regId": "NOC123456",
                "regDate": "10-10-2025",
            },
            {
                "name": "Test Inst 2",
                "regId": "NOC789456",
                "regDate": "20-12-2025",
            },
        ],
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Inprocess Application Data",
        "data": data,
    }
    return result

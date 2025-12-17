from fastapi import APIRouter, status, Depends
from dtos.institution.docketNumberDTO import SetDocketNumberRequest
from helpers import response
from core.Dependencies.auth import get_current_user

router = APIRouter(prefix="/institution/docketNumber", tags=["Docket Number"])

@router.post("", response_model=response.APIResponse)
def set_docket_number(request:SetDocketNumberRequest,current_user: dict = Depends(get_current_user)):
    print(current_user)
    # nocRegId = current_user["stake_user"]

    data = {
        "inspection": [
            {
                "inspectionDate": "12-10-2025",
                "inspectionStatus": "Complete",
                "remarks": "Test Remarks",
                "inspectionDocument": "",
            },
            {
                "inspectionDate": "15-12-2025",
                "inspectionStatus": "Pending",
                "remarks": "",
                "inspectionDocument": "",
            },
        ]
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Inspection Data",
        "data": data,
    }
    return result

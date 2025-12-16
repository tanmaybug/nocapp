from fastapi import APIRouter, status, Depends
from helpers import response
from core.Dependencies.auth import get_current_user

router = APIRouter(prefix="/institution/TrackApplication", tags=["TrackApplication"])

@router.get("", response_model=response.APIResponse)
def get_application_track_data(current_user: dict = Depends(get_current_user)):
    
    print(current_user)
    # nocRegId = current_user["stake_user"]
    
    data = {
        "trackData": [
            {
                "object": "Form-1",
                "submitDate": "12-10-2025",
                "status": "Submitted",
                "remarks": "Test Remarks",
            },
            {
                "object": "Form-2",
                "submitDate": "14-10-2025",
                "status": "Submitted",
                "remarks": "Test Remarks",
            },
            {
                "object": "Form-3",
                "submitDate": "15-10-2025",
                "status": "Submitted",
                "remarks": "Test Remarks",
            },
        ]
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Application Track Data",
        "data": data,
    }
    return result

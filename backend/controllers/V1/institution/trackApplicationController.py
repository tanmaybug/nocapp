from fastapi import APIRouter, status, Depends, HTTPException
from mappers.institution.applicationTrackMapper import application_track_response_dto
from helpers import response
from core.Dependencies.auth import get_current_user
from services.institution.applicationDetailsRepo import applicationDetailsService
from config.DB.DBConfig import get_db
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from services.institution.applicationTrackRepo import applicationTrackService

router = APIRouter(prefix="/institution/TrackApplication", tags=["TrackApplication"])


@router.get("", response_model=response.APIResponse)
def get_application_track_data(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    print(current_user)
    nocRegId = current_user["stake_user"]

    application_db_data = applicationDetailsService(db).get_application_data_by_id(
        nocRegId
    )
    if not application_db_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Record not found"
        )

    track_data = jsonable_encoder(
        applicationTrackService(db).get_track_data_by_applicant_id(nocRegId)
    )
    print(track_data)
    # data = application_track_response_dto(track_data)
    data = {
        "trackData": [
            {
                "sno": 1,
                "activity": "Registration Done",
                "date": "12-10-2025",
                "remarks": "",
            },
            {
                "sno": 2,
                "activity": "Final Submit Done",
                "date": "14-10-2025",
                "remarks": "",
            },
            {
                "sno": 3,
                "activity": "Docket Number Added",
                "date": "20-10-2025",
                "remarks": "",
            },
            {
                "sno": 4,
                "activity": "Inspection Date Assigned",
                "date": "20-10-2025",
                "remarks": "",
            },
        ],
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Application Track Data",
        "data": data,
    }
    return result

from fastapi import APIRouter, status, Depends, HTTPException
from helpers import response
from core.Dependencies.auth import get_current_user
from helpers.dateHelper import date_format
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
    # print(f"track data : {track_data}")

    formatted_track_data = [
        {
            "sno": index,
            "activity": item.get("remarks", ""),
            "date": date_format(item.get("insert_date", "")),
            "remarks": "",
        }
        for index, item in enumerate(track_data, start=1)
    ]

    # print(formatted_track_data)

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Application Track Data",
        "data": formatted_track_data,
    }
    return result

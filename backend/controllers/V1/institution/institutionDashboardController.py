from fastapi import APIRouter, status, Depends, HTTPException
from helpers import response
from core.Dependencies.auth import get_current_user
from services.institution.applicationDetailsRepo import applicationDetailsService
from services.institution.applicationTrackRepo import applicationTrackService
from config.DB.DBConfig import get_db
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/institution/Dashboard", tags=["Dashboard"])


@router.get("", response_model=response.APIResponse)
def get_dashboard_data(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # print(current_user)
    nocRegId = current_user["stake_user"]

    application_db_data = applicationDetailsService(db).get_application_data_by_id(
        nocRegId
    )
    # print(jsonable_encoder(application_db_data))
    if not application_db_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Record not found"
        )
    application_data = jsonable_encoder(application_db_data)

    track_db_data = applicationTrackService(db).get_track_data_by_applicant_id(
        nocRegId
    )
    track_data = jsonable_encoder(track_db_data)
    
    last_update = max(track_data, key=lambda x: x["insert_date"])
    final_submit_date = next(
        item["insert_date"] for item in track_data if item["status"] == 2
    )
    docket_date = next(
        item["insert_date"] for item in track_data if item["status"] == 3
    )

    data = {
        "currentStatus": application_data["status_description"],
        "lastUpdatedDate": last_update["insert_date"],
        "inspectionDate": application_data["NocApplicationDetails"]["inspection_date"],
        "isNOCCompleted": True
        if application_data["NocApplicationDetails"]["form_status"] == 7
        else False,
        "activities": [
            {
                "sno": 1,
                "activity": "Registration",
                "date": application_data["NocApplicationDetails"]["insert_time"],
                "status": "COMPLETED",
            },
            {
                "sno": 2,
                "activity": "Form-1",
                "date": "",
                "status": "COMPLETED"
                if application_data["NocApplicationDetails"]["form_status"] >= 1
                else "PENDING",
            },
            {
                "sno": 3,
                "activity": "Form-2",
                "date": "",
                "status": "COMPLETED"
                if application_data["NocApplicationDetails"]["form_status"] >= 2
                else "PENDING",
            },
            {
                "sno": 4,
                "activity": "Form-3",
                "date": "",
                "status": "COMPLETED"
                if application_data["NocApplicationDetails"]["form_status"] >= 3
                else "PENDING",
            },
            {
                "sno": 5,
                "activity": "Final Submition",
                "date": final_submit_date,
                "status": "COMPLETED"
                if application_data["NocApplicationDetails"]["application_status"] >= 2
                else "PENDING",
            },
            {
                "sno": 6,
                "activity": "Docket Number Added",
                "date": docket_date,
                "status": "COMPLETED"
                if application_data["NocApplicationDetails"]["application_status"] >= 3
                else "PENDING",
            },
        ],
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Dashbord Data",
        "data": data,
    }
    return result

from fastapi import APIRouter, status, Depends, HTTPException
from dtos.department.docketNumberDTO import SetDocketNumberRequest
from helpers import response
from core.Dependencies.auth import get_current_admin
from mappers.applicationTrackMapper import dtotodb as applicationTrackMap
from mappers.department.applicationMapper import (
    docket_number_update_dtotodb as applicationMap,
) 
from utils.iP import get_client_ip
from services.department.docketRepo import docketService
from config.DB.DBConfig import get_db
# from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

router = APIRouter(prefix="/department/docketNumber", tags=["Docket Number"])

@router.post("", response_model=response.APIResponse)
def set_docket_number(
    request: SetDocketNumberRequest,
    current_user: dict = Depends(get_current_admin),
    client_ip: str = Depends(get_client_ip),
    db: Session = Depends(get_db),
):
    # print(request.docketNumber)
    # print(request.nocRegId)
    nocRegId = request.nocRegId

    application_db_data = docketService(db).get_application_data_by_id_for_docket(
        nocRegId
    )
    if not application_db_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Record not found"
        )
    
    application_data = applicationMap(application_db_data,request.docketNumber)

    track_data = applicationTrackMap(
        {
            "nocRegId": nocRegId,
            "remarks": "Docket Number Submitted",
            "status": 3,
            "ip": client_ip,
        }
    )
    insert_status = docketService(db).insert_data(application_data, track_data)

    if insert_status:
        result = {
            "status_code": status.HTTP_200_OK,
            "message": "Docket Number Added",
            "data": "",
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Please Try Again",
        )
    return result
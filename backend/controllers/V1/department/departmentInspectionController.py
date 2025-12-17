from fastapi import APIRouter, status, Depends, UploadFile,HTTPException
from dtos.department.inspectionRequestDTO import (
    SetInspectionRequest,
    InspectionFeedbackRequest,
)
from config.DB.DBConfig import get_db
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from helpers import response
from core.Dependencies.auth import get_current_admin
from utils.iP import get_client_ip
from mappers.department.inspectionMapper import dtotodb_insert as inspectionMap
from mappers.department.inspectionMapper import dtotodb_update as inspectionUpdateMap
from services.department.inspectionRepo import inspectionService

router = APIRouter(prefix="/department/Inspection", tags=["Inspection"])

@router.post("/setInspectionDate", response_model=response.APIResponse)
def set_inspection_date(
    request: SetInspectionRequest,
    current_user: dict = Depends(get_current_admin),
    client_ip: str = Depends(get_client_ip),
    db: Session = Depends(get_db),
):
    print(current_user)
    print(request)
    userId = current_user["stake_user"]

    inspection_data = inspectionMap(request, userId, client_ip)

    insert_status = inspectionService(db).insert_data(inspection_data)

    if insert_status:
        result = {
            "status_code": status.HTTP_200_OK,
            "message": "Inspection Date has been Inserted Successfully",
            "data": "",
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Please Try Again",
        )
    return result

@router.get("/getInspectionTrack", response_model=response.APIResponse)
def get_inspection_track(
    nocRegId: str,
    current_user: dict = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    # print(current_user)
    print(nocRegId)
    # userId = current_user["stake_user"]

    inspection_data = jsonable_encoder(inspectionService(db).get_data(nocRegId))

    data = {
        "inspectionData": inspection_data,
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Get Inspection Data",
        "data": data,
    }
    return result

@router.post("/addInspectionFeedback", response_model=response.APIResponse)
def add_inspection_feedback(
    request: InspectionFeedbackRequest,
    current_user: dict = Depends(get_current_admin),
    client_ip: str = Depends(get_client_ip),
    db: Session = Depends(get_db),
):
    print(current_user)
    print(request)
    # userId = current_user["stake_user"]

    nocRegId = request.nocRegId
    inspection_data = jsonable_encoder(inspectionService(db).get_data(nocRegId))

    inspection_data = inspectionUpdateMap(request, client_ip)
    print(inspection_data)

    data = {
        "totalPendingApplication": 10,
        "totalInProcessApplication": 20,
        "totalNocCompleteApplication": 30,
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Add Inspection Feedback Data",
        "data": data,
    }
    return result

@router.post("/addInspectionDocument", response_model=response.APIResponse)
def add_inspection_document(
    file: UploadFile, current_user: dict = Depends(get_current_admin)
):
    print(current_user)
    
    # userId = current_user["stake_user"]

    data = {
        "totalPendingApplication": 10,
        "totalInProcessApplication": 20,
        "totalNocCompleteApplication": 30,
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Add Inspection Document",
        "data": data,
    }
    return result
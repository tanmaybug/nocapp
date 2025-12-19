from fastapi import APIRouter, status, Depends, UploadFile, HTTPException
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
from mappers.department.inspectionMapper import (
    dtotodb_insert as inspectionMap,
    dtotodb_update as inspectionUpdateMap,
    dtotodb_document_update as inspectionDocumentUpdateMap,
    dtotodb_inspection_date_update as inspectionDateUpdateMap,
)
from services.department.inspectionRepo import inspectionService
from services.department.applicationRepo import applicationService

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

    nocRegId = request.nocRegId
    application_db_data = applicationService(db).get_application_data_by_id(nocRegId)
    if not application_db_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Record not found"
        )

    application_data = inspectionDateUpdateMap(application_db_data, request.date)

    inspection_data = inspectionMap(request, userId, client_ip)

    insert_status = inspectionService(db).insert_data(
        inspection_data, application_data
    )

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
    db: Session = Depends(get_db),
):
    print(current_user)
    print(request)
    # userId = current_user["stake_user"]

    nocRegId = request.nocRegId
    inspection_db_data = inspectionService(db).get_data(nocRegId)
    if not inspection_db_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Record not found"
        )

    inspection_data = inspectionUpdateMap(request, inspection_db_data)
    update_status = inspectionService(db).update_data(inspection_data)

    if update_status:
        result = {
            "status_code": status.HTTP_200_OK,
            "message": "Feedback Submited Successfully",
            "data": "",
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Updation Failed.Please Try Again",
        )

    return result


@router.post("/addInspectionDocument", response_model=response.APIResponse)
def add_inspection_document(
    file: UploadFile,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_admin),
):
    print(current_user)
    # userId = current_user["stake_user"]
    file_path = "test.pdf"

    nocRegId = "NOC123"
    inspection_db_data = inspectionService(db).get_data(nocRegId)
    if not inspection_db_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Record not found"
        )

    inspection_data = inspectionDocumentUpdateMap(inspection_db_data, file_path)
    update_status = inspectionService(db).update_data(inspection_data)

    if update_status:
        result = {
            "status_code": status.HTTP_200_OK,
            "message": "Feedback Document Update Successfully",
            "data": "",
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Updation Failed.Please Try Again",
        )

    return result

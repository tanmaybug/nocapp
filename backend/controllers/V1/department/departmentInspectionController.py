from fastapi import APIRouter, status, Depends, UploadFile
from dtos.department.inspectionRequestDTO import (
    SetInspectionRequest,
    InspectionFeedbackRequest,
)
from helpers import response
from core.Dependencies.auth import get_current_admin

router = APIRouter(prefix="/department/Inspection", tags=["Inspection"])


@router.post("/setInspectionDate", response_model=response.APIResponse)
def set_inspection_date(request:SetInspectionRequest,current_user: dict = Depends(get_current_admin)):
    print(current_user)
    print(request)
    # userId = current_user["stake_user"]

    data = {
        "totalPendingApplication": 10,
        "totalInProcessApplication": 20,
        "totalNocCompleteApplication": 30,
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Set Inspection Date",
        "data": data,
    }
    return result

@router.get("/getInspectionTrack", response_model=response.APIResponse)
def get_inspection_track(
    nocRegId: str, current_user: dict = Depends(get_current_admin)
):
    print(current_user)
    print(nocRegId)
    # userId = current_user["stake_user"]

    data = {
        "totalPendingApplication": 10,
        "totalInProcessApplication": 20,
        "totalNocCompleteApplication": 30,
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Get Inspection Data",
        "data": data,
    }
    return result

@router.post("/addInspectionFeedback", response_model=response.APIResponse)
def add_inspection_feedback(
    request: InspectionFeedbackRequest, current_user: dict = Depends(get_current_admin)
):
    print(current_user)
    print(request)
    # userId = current_user["stake_user"]

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
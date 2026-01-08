from fastapi import APIRouter, status, Depends
from helpers import response
from core.Dependencies.auth import get_current_admin
from config.DB.DBConfig import get_db
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from services.department.applicationRepo import applicationService

router = APIRouter(prefix="/department/Dashboard", tags=["Dashboard"])

@router.get("", response_model=response.APIResponse)
def get_dashboard_data(
    current_user: dict = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    
    # print(current_user)
    # userId = current_user["stake_user"]
    pending_data = jsonable_encoder(
        applicationService(db).get_pending_application_data()
    )
    inprocess_data = jsonable_encoder(
        applicationService(db).get_inprocess_application_data()
    )
    complete_data = jsonable_encoder(
        applicationService(db).get_complete_application_data()
    )

    data = {
        "totalPendingApplication": len(pending_data),
        "totalInProcessApplication": len(inprocess_data),
        "totalNocCompleteApplication": len(complete_data),
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Department Dashboard Data",
        "data": data,
    }
    return result
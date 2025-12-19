from fastapi import APIRouter, status, Depends
from helpers import response
from core.Dependencies.auth import get_current_admin
from config.DB.DBConfig import get_db
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from services.department.applicationRepo import applicationService

router = APIRouter(
    prefix="/department/InprocessApplication", tags=["Report"]
)

@router.get("", response_model=response.APIResponse)
def get_application_data(
    current_user: dict = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    print(current_user)
    # userId = current_user["stake_user"]

    pending_data = jsonable_encoder(
        applicationService(db).get_inprocess_application_data()
    )
    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Inprocess Application Data",
        "data": pending_data,
    }
    return result
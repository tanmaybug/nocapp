from fastapi import APIRouter, status, Depends
from core.Dependencies.auth import get_current_user
from helpers import response
from config.DB.DBConfig import get_db
from sqlalchemy.orm import Session
# from fastapi.encoders import jsonable_encoder
# from services.studentRepo import studentService
# from mappers.studentTableMapper import dbtodto

router = APIRouter(prefix="/noc_application", tags=["NOC_Application"])


@router.get("/", response_model=response.APIResponse)
def get_master_data(
    current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)
):  
    result = {
        "status_code": status.HTTP_200_OK,
        "message": "User Data",
        "data": current_user,
    }
    return result


@router.get("/get_data", response_model=response.APIResponse)
def get_data(
    current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Get Data",
        "data": current_user,
    }
    return result

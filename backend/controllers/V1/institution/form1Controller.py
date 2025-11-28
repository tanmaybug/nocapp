from fastapi import APIRouter, HTTPException,status
from fastapi.params import Depends
from dtos.form1DTOcg import Form1
from sqlalchemy.orm import Session
from config.DB.DBConfig import get_db
from mappers.form1Mapper import dtotodb as form1Map
from helpers import response
from services.form1Repo import form1Service
# from core.Dependencies.auth import get_current_user

router = APIRouter(prefix="/form1", tags=["Form"])

@router.post("/", response_model=response.APIResponse)
def submit_application_data(
    request: Form1,
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user),
):
    # print(request)
    # print(current_user)
    # nocRegId = current_user["stake_user"]
    nocRegId = "NOC20251121102258"
    form1_data = form1Map(request, nocRegId)
    insert_status = form1Service(db).insert_data(
        form1_data
    )

    if insert_status:
        data = {"nocRegId": nocRegId}
        result = {
            "status_code": status.HTTP_200_OK,
            "message": "Form1 Successfully Submitted",
            "data": data,
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Form1 Submission Failed.Please Try Again",
        )
    return result
        

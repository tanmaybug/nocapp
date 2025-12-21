from fastapi import APIRouter, HTTPException, status, Depends
from dtos.form1DTOcg import Form1
from sqlalchemy.orm import Session
from config.DB.DBConfig import get_db
from mappers.form1Mapper import dtotodb_update as form1Map
from helpers import response
from services.form1Repo import form1Service
from core.Dependencies.auth import get_current_user
from services.institution.applicationDetailsRepo import applicationDetailsService

router = APIRouter(prefix="/institution/form1", tags=["Form"])

@router.post("", response_model=response.APIResponse)
def update_application_data(
    request: Form1,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    print(request)
    print(current_user)
    nocRegId = current_user["stake_user"]
    
    
    application_db_data = applicationDetailsService(db).get_application_data_by_id(nocRegId)
    if not application_db_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Record not found"
        )
    
    # Step 2: Use mapper to update the record
    updated_record = form1Map(request, application_db_data)
    update_status = form1Service(db).update_data(updated_record)

    if update_status:
        data = {"nocRegId": nocRegId}
        result = {
            "status_code": status.HTTP_200_OK,
            "message": "Form1 Updated Successfully",
            "data": data,
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Form1 Updation Failed.Please Try Again",
        )
    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Form1 Updated Successfully",
        "data": "",
    }
    return result
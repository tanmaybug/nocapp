from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from dtos.form2DTO import Form2
from sqlalchemy.orm import Session
from config.DB.DBConfig import get_db
from mappers.form2Mapper import updatedb as form2Map
from helpers import response
from services.form2Repo import form2Service
# from core.Dependencies.auth import get_current_user

router = APIRouter(prefix="/form2", tags=["Form"])

@router.post("/", response_model=response.APIResponse)
def update_application_data(
    request: Form2,
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user),
):
    nocRegId = "NOC20251121102258"
    # nocRegId = current_user["stake_user"]

    record = form2Service(db).get_data(nocRegId)

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Record not found"
        )

    # Step 2: Use mapper to update the record
    updated_record = form2Map(request, record)
    update_status = form2Service(db).update_data(updated_record)

    if update_status:
        data = {"nocRegId": nocRegId}
        result = {
            "status_code": status.HTTP_200_OK,
            "message": "Form2 Updated Successfully",
            "data": data,
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Form2 Updation Failed.Please Try Again",
        )

    return result

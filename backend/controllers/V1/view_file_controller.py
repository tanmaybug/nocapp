from fastapi import APIRouter, status, Depends, HTTPException
from helpers import response
from config.DB.DBConfig import get_db
# from core.Dependencies.auth import get_current_user
from sqlalchemy.orm import Session

from services.fileRepo import fileService

router = APIRouter(prefix="/viewFile", tags=["View File"])


@router.get("", response_model=response.APIResponse)
def get_file_data(
    fileId: int,
    # current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    file_data = fileService(db).get_data(fileId)
    if not file_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="File not found"
        )
    
    
    # data = {"Id": 1, "Details": "Test2 Details from test controller"}

    result = response.APIResponse(
        status_code=status.HTTP_200_OK, message="Test Response", data=file_data
    )
    return result

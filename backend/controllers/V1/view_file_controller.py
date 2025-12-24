from fastapi import APIRouter, status, Depends, HTTPException
from helpers import response
from config.DB.DBConfig import get_db
from core.Dependencies.auth import get_current_user_admin
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from services.fileRepo import fileService
from fastapi.responses import FileResponse, StreamingResponse
from config.config import settings

router = APIRouter(prefix="/viewFile", tags=["View File"])


@router.get("", response_model=response.APIResponse)
def get_file_data(
    fileId: int,
    current_user: dict = Depends(get_current_user_admin),
    db: Session = Depends(get_db),
):
    file_db_data = fileService(db).get_data(fileId)
    if not file_db_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="File not found"
        )

    file_data = jsonable_encoder(file_db_data)
    # print(file_data)

    data = {
        "Id": file_data["upload_document_id_pk"],
        "fileType": "application/pdf",
        "fileName": file_data["uploaded_document_name"],
    }

    result = response.APIResponse(
        status_code=status.HTTP_200_OK, message="Test Response", data=data
    )
    return result


@router.get("/downloadFile")
def download_file(
    fileId: int,
    current_user: dict = Depends(get_current_user_admin),
    db: Session = Depends(get_db),
):
    print(current_user)
    file_db_data = fileService(db).get_data(fileId)
    if not file_db_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="File not found"
        )

    file_data = jsonable_encoder(file_db_data)

    file_path = settings.UPLOADS_DIR / file_data["uploaded_document_name"]
    return FileResponse(
        path=file_path,
        media_type="application/pdf",
        filename=file_data["uploaded_document_name"],
    )


@router.get("/downloadLargeFile")
def download_large_file(
    fileId: int,
    current_user: dict = Depends(get_current_user_admin),
    db: Session = Depends(get_db),
):
    file_db_data = fileService(db).get_data(fileId)
    if not file_db_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="File not found"
        )

    file_data = jsonable_encoder(file_db_data)
    file_path = settings.UPLOADS_DIR / file_data["uploaded_document_name"]
    return StreamingResponse(
        iterfile(file_path),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=sample.pdf"},
    )


def iterfile(path: str):
    with open(path, "rb") as file:
        while chunk := file.read(1024 * 1024):
            yield chunk

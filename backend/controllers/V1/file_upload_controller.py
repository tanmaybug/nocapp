from fastapi import APIRouter, status, UploadFile, HTTPException
from pathlib import Path
import shutil
import uuid

# from dtos.fileUploadDTO import FileUploadDTO
from helpers import response
from utils.customFileValidation import validatePDF


router = APIRouter(prefix="/fileUpload", tags=["FileUpload"])


@router.post("/", response_model=response.APIResponse)
def submit_data(file: UploadFile):
    # print(file)

    UPLOAD_DIR = Path("../uploads")
    UPLOAD_DIR.mkdir(exist_ok=True)

    if validatePDF(file):
        if not file.filename:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Filename is empty.",
            )
        file_ext = Path(file.filename).suffix
        if not file_ext:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="File has no extension.",
            )

        # file_path = UPLOAD_DIR / file.filename

        # Create unique filename
        file_ext = Path(file.filename).suffix
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        file_path = UPLOAD_DIR / unique_filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        uploadedFilePath = Path(file_path)
        if uploadedFilePath.exists():
            data = {"file_name": unique_filename, "file_type": file.content_type}

    else:
        data = {"file_name": "Invalid File"}

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Test Response",
        "data": data,
    }
    return result

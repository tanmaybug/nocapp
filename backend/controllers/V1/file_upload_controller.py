from fastapi import APIRouter, status, UploadFile
from pathlib import Path
import shutil
import uuid
# from dtos.fileUploadDTO import FileUploadDTO
from helpers import response
from utils.customFileValidation import validate


router = APIRouter(prefix="/fileUpload", tags=["FileUpload"])


@router.post("/", response_model=response.APIResponse)
def submit_data(file: UploadFile):
    # print(file)

    UPLOAD_DIR = Path("../uploads")
    UPLOAD_DIR.mkdir(exist_ok=True)
    
    if validate(file):
        data = {"file_name": file.filename, "file_type": file.content_type}

        # file_path = UPLOAD_DIR / file.filename

        # Create unique filename
        file_ext = Path(file.filename).suffix
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        file_path = UPLOAD_DIR / unique_filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    else:
        data = {"file_name": "Invalid File"}
        
    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Test Response",
        "data": data,
    }
    return result

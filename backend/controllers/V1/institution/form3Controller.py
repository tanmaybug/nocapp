from fastapi import APIRouter, status, UploadFile, HTTPException, Depends
from utils.iP import get_client_ip
from services.form3Repo import form3Service
from helpers import response
from utils.customFileValidation import validatePDF
from mappers.uploadDocumentTableMapper import dtotodb
from pathlib import Path
import shutil
import uuid
import base64
from config.DB.DBConfig import get_db
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
# from core.Dependencies.auth import get_current_user

router = APIRouter(prefix="/form3", tags=["Form"])

@router.post("/", response_model=response.APIResponse)
def upload_file(
    file: UploadFile,
    db: Session = Depends(get_db),
    client_ip: str = Depends(get_client_ip),
    # current_user: dict = Depends(get_current_user),
):
    print(f"client ip: {client_ip}")

    UPLOAD_DIR = Path("../uploads")
    UPLOAD_DIR.mkdir(exist_ok=True)
    # nocRegId = current_user["stake_user"]
    nocRegId = "NOC20251121102258"

    if validatePDF(file):
        # Create unique filename
        file_ext = Path(file.filename).suffix
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        file_path = UPLOAD_DIR / unique_filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        uploadedFilePath = Path(file_path)
        if uploadedFilePath.exists():
            uploadDataMap = dtotodb(
                {
                    "regId": nocRegId,
                    "documentId": 1,
                    "documentName": unique_filename,
                    "ip": client_ip,
                }
            )
            insert_status = form3Service(db).insert_data(uploadDataMap)
            if insert_status:
                insertData = jsonable_encoder(insert_status)
                # base64Data = file_to_base64(uploadedFilePath)
                # print(f"Base64 data : {base64Data}")
                data = {
                    "fileName": unique_filename,
                    "fileType": file.content_type,
                    "fileId": insertData["upload_document_id_pk"],
                }
                result = {
                    "status_code": status.HTTP_200_OK,
                    "message": "Test Response",
                    "data": data,
                }          
        else:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="File Not Uploaded.Please Try Again",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Please Upload Valid PDF File",
        )
    return result


def file_to_base64(file_path):
    try:
        with open(file_path, "rb") as file:
            binary_data = file.read()
            base64_encoded_data = base64.b64encode(binary_data)
            # Decode to string for easier handling, typically using 'ascii'
            base64_string = base64_encoded_data.decode("ascii")
            return base64_string
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None 
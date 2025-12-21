from fastapi import APIRouter, status, HTTPException, Depends, UploadFile
from services.institution.fileRepo import FileService
from dtos.institution.fileUploadDTO import SaveFileRequest
from utils.iP import get_client_ip
from services.form3Repo import form3Service
from helpers import response
from utils.customFileValidation import validatePDF
from mappers.uploadDocumentTableMapper import dtotodb, save_file_dtotodb
from pathlib import Path
import shutil
import uuid
import base64
from config.DB.DBConfig import get_db
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from core.Dependencies.auth import get_current_user

router = APIRouter(prefix="/institution", tags=["Form"])


@router.post("", response_model=response.APIResponse)
def submit():
    nocRegId = "NOC20251121102258"
    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Form3 Successfully Submitted",
        "data": nocRegId,
    }
    return result


@router.post("/fileUpload", response_model=response.APIResponse)
def upload_file(
    file: UploadFile,
    db: Session = Depends(get_db),
    client_ip: str = Depends(get_client_ip),
    current_user: dict = Depends(get_current_user),
):
    print(f"client ip: {client_ip}")

    UPLOAD_DIR = Path("../uploads")
    UPLOAD_DIR.mkdir(exist_ok=True)
    nocRegId = current_user["stake_user"]
    # nocRegId = "NOC20251121102258"

    if validatePDF(file):
        if not file.filename:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Filename is empty.",
            )
        # Create unique filename
        file_ext = Path(file.filename).suffix
        if not file_ext:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="File has no extension.",
            )
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        file_path = UPLOAD_DIR / unique_filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        uploadedFilePath = Path(file_path)
        if uploadedFilePath.exists():
            uploadDataMap = dtotodb(
                {
                    "regId": nocRegId,
                    "documentId": 0,
                    "documentName": unique_filename,
                    "ip": client_ip,
                }
            )
            # print(jsonable_encoder(uploadDataMap))
            insert_status = form3Service(db).insert_data(uploadDataMap)
            if insert_status:
                insertData = jsonable_encoder(insert_status)
                # base64Data = file_to_base64(uploadedFilePath)
                # print(f"Base64 data : {base64Data}")
                data = {
                    "fileName": unique_filename,
                    "fileUrl": "https://banglaruchchashiksha.wb.gov.in/assets/readwrite/uploads/E_Governance_Final_Book.pdf",
                    "fileId": insertData["upload_document_id_pk"],
                }
                result = {
                    "status_code": status.HTTP_200_OK,
                    "message": "File Upload Success",
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


@router.post("/saveFile", response_model=response.APIResponse)
def save_file(
    request: SaveFileRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    nocRegId = current_user["stake_user"]
    fileId = request.fileId
    file_db_data = FileService(db).get_unsaved_data(fileId, nocRegId)
    if not file_db_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Record not found"
        )

    file_data = save_file_dtotodb(file_db_data, request.documentTypeId)
    update_status = FileService(db).update_doc_type(file_data)
    if update_status:
        result = {
            "status_code": status.HTTP_200_OK,
            "message": "File Saved Successfully",
            "data": "",
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Submission Failed.Please Try Again",
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

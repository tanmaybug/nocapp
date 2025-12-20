from pydantic import BaseModel
from fastapi import UploadFile

class FileUploadRequest(BaseModel):
    file: UploadFile

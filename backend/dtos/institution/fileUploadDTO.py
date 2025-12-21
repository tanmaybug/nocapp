from pydantic import BaseModel
from fastapi import UploadFile

class FileUploadRequest(BaseModel):
    file: UploadFile


class SaveFileRequest(BaseModel):
    fileId: int
    documentType:str
    documentTypeId:int

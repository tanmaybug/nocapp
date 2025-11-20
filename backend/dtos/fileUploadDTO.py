from pydantic import BaseModel

class FileUploadDTO(BaseModel):
    file_path:str
    file_name:str
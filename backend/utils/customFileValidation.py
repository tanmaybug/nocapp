from fastapi import UploadFile, HTTPException, status
from config.config import settings

def validate(file: UploadFile):
    # file_type = file.content_type
    # print(file.size)

    MAX_FILE_SIZE = settings.MAX_FILE_SIZE  
    MIN_FILE_SIZE = settings.MIN_FILE_SIZE  

    accepted_file_types = [
        "image/png",
        "image/jpeg",
        "image/jpg",
        "png",
        "jpeg",
        "jpg",
    ]

    if file.content_type not in accepted_file_types:
        print("type error")
        return False
    elif file.size is not None and file.size > MAX_FILE_SIZE and file.size < MIN_FILE_SIZE:
        print("size error")
        return False
    else:
        return True
    
def validatePDF(file: UploadFile):
    # file_type = file.content_type
    # print(file.size)

    MAX_FILE_SIZE = settings.MAX_PDF_FILE_SIZE
    MIN_FILE_SIZE = settings.MIN_PDF_FILE_SIZE

    accepted_file_types = [
        "application/pdf",
        "pdf",
        "PDF",
    ]

    if file.content_type not in accepted_file_types:
        print("type error")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Please Upload PDF File",
        )
    elif (
        file.size is not None
        and file.size > MAX_FILE_SIZE
        and file.size < MIN_FILE_SIZE
    ):
        print("size error")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="File Size Error",
        )
    else:
        return True
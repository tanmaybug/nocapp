from fastapi import APIRouter, status, Depends
from dtos.testFormDTO import TestFormRequestDTO
from helpers import response
from config.DB.DBConfig import get_db
from sqlalchemy.orm import Session
from mappers.testTableMapper import dtotodb
# from models.testTableModel import Post
# from repos.testFormRepo import adddata
from services.testFormRepo import testService

router = APIRouter(prefix="/form", tags=["Form"])

@router.post("/", response_model=response.APIResponse)
def submit_data(request: TestFormRequestDTO,db: Session = Depends(get_db)):
    # print(request)
    # data = request

    # form_data = {
    #     "name": request.name,
    #     "phone": request.phone_number,
    #     "email": request.email,
    #     "create_ip": "127.0.0.1",
    # }
    
    new_post = dtotodb(request)
    testService(db).adddata(new_post)

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Test Response",
        "data": '',
    }
    return result
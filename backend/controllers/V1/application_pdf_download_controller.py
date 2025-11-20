from fastapi import APIRouter, status, Depends
from helpers import response
from config.DB.DBConfig import get_db
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from services.studentRepo import studentService
from mappers.studentTableMapper import dbtodto

router = APIRouter(prefix="/login", tags=["Login"])


@router.get("/", response_model=response.APIResponse)
def get_all_student_data(db: Session = Depends(get_db)):
    db_data = jsonable_encoder(studentService(db).get_data())

    students = dbtodto(db_data)
    result = {
        "status_code": status.HTTP_200_OK,
        "message": "List Of All Students",
        "data": students,
    }
    return result

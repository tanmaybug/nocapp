from typing import Any
from fastapi import APIRouter, status, Depends, HTTPException
from dtos.loginFormDTO import LoginFormRequestDTO
from helpers import response
from config.DB.DBConfig import get_db
from sqlalchemy.orm import Session

from services.loginRepo import loginService
from utils.password import verify_password
from utils.token import create_token

router = APIRouter(prefix="/login", tags=["Login"])


@router.post("/", response_model=response.APIResponse)
def login(request: LoginFormRequestDTO, db: Session = Depends(get_db)):
    db_data: Any = loginService(db).get_data(request.username)

    if db_data:
        password = db_data["stake_password"]
        if verify_password(request.password, password):
            token = create_token(
                db_data["stake_user"],
                db_data["login_id_pk"],
                db_data["stake_level_id_fk"],
            )
            # loginService(db).update_token(db_data["stake_user"],token)
            if db_data["stake_level_id_fk"] == 1:
                role = "ADMIN"
                userName = "State"
            elif db_data["stake_level_id_fk"] == 2:
                role = "ADMIN"
                userName = "Department"
            elif db_data["stake_level_id_fk"] == 3:
                role = "INSTITUTION"
                userName = "Institution"
            else:
                role = ""
                userName = ""

            login_data = {"token": token, "role": role, "name": userName}
            result = {
                "status_code": status.HTTP_200_OK,
                "message": "Login Success",
                "data": login_data,
            }
            return result
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Wrong Username and Password",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong Username and Password",
        )

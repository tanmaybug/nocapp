from fastapi import APIRouter, status, Depends
from helpers import response
from core.Dependencies.auth import get_current_user_admin

router = APIRouter(prefix="/checkTokenValidity", tags=["Token Validity"])

@router.get("/")
def check_token(current_user: dict = Depends(get_current_user_admin)):
    print(current_user)
    result = response.APIResponse(
        status_code=status.HTTP_200_OK, message="Token Validity"
    )
    return result

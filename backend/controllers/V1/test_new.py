from fastapi import APIRouter, status
from helpers import response

router = APIRouter(prefix="/test", tags=["Test"])

@router.get("/")
def get_data_test2():
    data = {"Id": 1, "Details": "Test2 Details from test controller"}

    result = response.APIResponse(
        status_code=status.HTTP_200_OK, message="Test Response", data=data
    )
    return result

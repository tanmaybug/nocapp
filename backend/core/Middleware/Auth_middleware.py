from fastapi import Request, status
from fastapi.responses import JSONResponse

from utils.token import validate_token, decode_token


async def auth_middleware(request: Request, call_next):
    protected_paths = [
        "/v1/form1",
        "/v1/form2",
        "/v1/form3",
        "/v1/institution/Dashboard",
        "/v1/institution/TrackApplication",
        "/v1/institution/Inspection",
        "/v1/institution/docketNumber",
        "/v1/institution/NOCApplication",
        "/v1/institution/NOCApplication/test",
        "/v1/institution/NOCApplication/download",
        "/v1/department/Dashboard",
        "/v1/department/ViewApplication",
        "/v1/department/ViewApplication/download",
        "/v1/department/Inspection/setInspectionDate",
        "/v1/department/Inspection/getInspectionTrack",
        "/v1/department/Inspection/addInspectionFeedback",
        "/v1/department/Inspection/addInspectionDocument",
        "/v1/department/PendingApplication",
        "/v1/department/InprocessApplication",
        "/v1/department/CompleteApplication",
    ]

    # Only protect exact matches
    if any(request.url.path.startswith(prefix) for prefix in protected_paths):
        token = request.headers.get("Authorization")
        
        if token and validate_token(token.split(" ")[1]):
            user_data = decode_token(token.split(" ")[1])
            print(user_data)
            request.state.user = user_data
        else:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Unauthorized"},
            )
        
    response = await call_next(request)
    return response

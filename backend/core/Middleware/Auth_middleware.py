from fastapi import Request, status
from fastapi.responses import JSONResponse

from utils.token import validate_token, decode_token


async def auth_middleware(request: Request, call_next):
    if request.method == "OPTIONS":
        return await call_next(request)
    
    protected_paths = [
        "/v1/institution/form1",
        "/v1/institution/form2",
        "/v1/institution/form3",
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
        "/v1/department/noc-applications/pending",
        "/v1/department/noc-applications/in-process",
        "/v1/department/noc-applications/completed",
    ]

    # url_token_allow_path = ["/v1/institution/NOCApplication/download","/v1/department/ViewApplication/download",]

    # Only protect exact matches
    if any(request.url.path.startswith(prefix) for prefix in protected_paths):
        token = request.headers.get("Authorization")
        if token:
            if token and validate_token(token.split(" ")[1]):
                user_data = decode_token(token.split(" ")[1])
                # print(f"Auth middle:{user_data}")
                request.state.user = user_data
            else:
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content={"detail": "Unauthorized"},
                )
        else:
            token = request.query_params.get("token")
            if token and validate_token(token):
                user_data = decode_token(token)
                # print(user_data)
                request.state.user = user_data
            else:
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content={"detail": "Unauthorized"},
                )
        
    response = await call_next(request)
    return response

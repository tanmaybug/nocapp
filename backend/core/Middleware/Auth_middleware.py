from fastapi import Request, status
from fastapi.responses import JSONResponse

from utils.token import validate_token, decode_token


async def auth_middleware(request: Request, call_next):
    protected_paths = ["/v1/noc_application/"]

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

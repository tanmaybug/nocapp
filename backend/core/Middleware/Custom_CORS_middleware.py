from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp
from typing import Callable


class CustomCORSMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, allowed_origins: list[str]):
        super().__init__(app)
        self.allowed_origins = allowed_origins

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        origin = request.headers.get("origin")
        print(origin)

        # Handle preflight request
        if request.method == "OPTIONS":
            if origin in self.allowed_origins:
                return Response(
                    status_code=204,
                    headers={
                        "Access-Control-Allow-Origin": origin,
                        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                        "Access-Control-Allow-Headers": "Authorization, Content-Type",
                        "Access-Control-Max-Age": "86400",
                    },
                )
            elif origin is None or origin == "null":
                return JSONResponse(
                    status_code=403,
                    content={"detail": "CORS policy blocks requests with null origin...."},
                )
            else:
                return JSONResponse(
                    status_code=403,
                    content={
                        "detail": "CORS policy does not allow access from this origin."
                    },
                )

        # Handle actual request
        response = await call_next(request)
        if origin in self.allowed_origins:
            response.headers["Access-Control-Allow-Origin"] = origin
        elif origin is None or origin == "null":
            return JSONResponse(
                status_code=403,
                content={"detail": "CORS policy blocks requests with null origin...."},
            )
        else:
            return JSONResponse(
                status_code=403,
                content={
                    "detail": "CORS policy does not allow access from this origin.."
                },
            )
        return response

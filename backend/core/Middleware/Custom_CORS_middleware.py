from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp
from typing import Callable
from config.config import settings


class CustomCORSMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, allowed_origins: list[str]):
        super().__init__(app)
        self.allowed_origins = allowed_origins
        print(f"allow origin {allowed_origins}")

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        origin = request.headers.get("origin")
        path = request.url.path
        
        print(f"reuest origin {origin}")
        print(f"reuest path {path}")

        # Block swagger in production env
        if settings.ENV == "production" and path.startswith(
            ("/api/docs", "/openapi.json")
        ):
            return JSONResponse(
                status_code=403,
                content={"detail": "Swagger is disabled in this environment"},
            )

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
                    content={"detail": "CORS policy blocks requests with null origin."},
                )
            else:
                return JSONResponse(
                    status_code=403,
                    content={
                        "detail": "CORS policy does not allow access from this origin.."
                    },
                )

        # Handle actual request
        response = await call_next(request)

        if (origin is None or origin == "null") and settings.ENV == "development":
            return response
    
        if origin in self.allowed_origins:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Vary"] = "Origin"

            return response
        else:
            return JSONResponse(
                status_code=403,
                content={
                    "detail": "CORS policy does not allow access from this origin..."
                },
            )
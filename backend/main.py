from fastapi import FastAPI
from config.config import settings
from config import router
from core.Middleware import Logging_middleware
from core.Middleware.Auth_middleware import auth_middleware
from core.Middleware import Custom_CORS_middleware
# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="NOC Portal",
    description="NOC Portal Backend",
    version="1.0.0",
    docs_url="/api/docs" if settings.ENV == "development" else None, # Custom Swagger UI URL
    redoc_url=None,
    openapi_url="/openapi.json" if settings.ENV == "development" else None,
)


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:5173",  # Vue dev server
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],  # GET, POST, PUT, DELETE, OPTIONS
#     allow_headers=["*"],  # Authorization, Content-Type, etc
# )

# Define allowed origins

BASE_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Vue
]

if settings.ENV == "development":
    BASE_ALLOWED_ORIGINS.extend(
        [
            "http://127.0.0.1:8000",
            "http://localhost:8000",
        ]
    )

allowed_origins = BASE_ALLOWED_ORIGINS

# Add the custom middleware
app.add_middleware(
    Custom_CORS_middleware.CustomCORSMiddleware, allowed_origins=allowed_origins
)

app.add_middleware(Logging_middleware.DateWiseLoggerMiddleware)
app.middleware("http")(auth_middleware)

app.include_router(router.master_router)


@app.get("/")
def get_data():
    return {"Details": "Details from Default Page...."}

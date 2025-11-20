from fastapi import FastAPI

from config import router
from core.Middleware import Logging_middleware
from core.Middleware.Auth_middleware import auth_middleware
# from core.Middleware import Custom_CORS_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="NOC Portal",
    description="NOC Portal Backend",
    version="1.0.0",
    docs_url="/api/docs",  # Custom Swagger UI URL
)

origins = [
    "*"  # Allows all origins
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Set to True if you need to support cookies, authorization headers, etc.
    allow_methods=["*"],     # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],     # Allows all headers in the request
)
# Define allowed origins
# allowed_origins = ["http://127.0.0.1:8000"]

# Add the custom middleware
# app.add_middleware(Custom_CORS_middleware.CustomCORSMiddleware, allowed_origins=allowed_origins)

app.add_middleware(Logging_middleware.DateWiseLoggerMiddleware)
app.middleware("http")(auth_middleware)

app.include_router(router.master_router)

@app.get("/")
def get_data():
    return {"Details": "Details from Default Page"}

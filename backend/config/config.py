from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from typing import ClassVar

class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DATABASE: str

    ENV:str
    FRONTEND_URL:str
    DEV_URL_1: str
    DEV_URL_2: str

    PROJECT_TITLE: str = "NOC"
    MAX_FILE_SIZE: int = 2097152  # 2MB
    MIN_FILE_SIZE: int = 1250  # 10KB

    MAX_PDF_FILE_SIZE: int = 2097152  # 2MB
    MIN_PDF_FILE_SIZE: int = 1250  # 10KB

    BASE_DIR: ClassVar[Path] = Path(__file__).resolve().parents[2]
    UPLOADS_DIR: ClassVar[Path] = BASE_DIR / "uploads"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")


settings = Settings()


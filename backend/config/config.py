from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DATABASE: str

    PROJECT_TITLE: str = "NOC"
    MAX_FILE_SIZE: int = 2097152  # 2MB
    MIN_FILE_SIZE: int = 1250  # 10KB

    MAX_PDF_FILE_SIZE: int = 2097152  # 2MB
    MIN_PDF_FILE_SIZE: int = 1250  # 10KB

    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")


settings = Settings()


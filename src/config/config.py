import os
from functools import cached_property
from pathlib import Path
from typing import Literal

from pydantic import AnyHttpUrl, EmailStr, PostgresDsn, computed_field
from pydantic_settings import BaseSettings

PROJECT_DIR = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    # CORE SETTINGS
    # SECRET_KEY: str
    ENVIRONMENT: Literal["DEV", "PYTEST", "STG", "PRD"] = "DEV"
    SECURITY_BCRYPT_ROUNDS: int = 12
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 11520  # 8 days
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 40320  # 28 days
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []
    ALLOWED_HOSTS: list[str] = ["localhost", "127.0.0.1"]

    # PROJECT NAME, VERSION AND DESCRIPTION
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    VERSION: str = os.getenv("VERSION")
    DESCRIPTION: str = os.getenv("DESCRIPTION")

    # SQL DATABASE
    SQL_DATABASE: str = os.getenv("SQL_DATABASE")

    # Mongo DATABASE
    MONGO_DATABASE: str = os.getenv("MONGO_DATABASE")

    # TEST_DATABASE_USER: str = "postgres"
    # TEST_DATABASE_PASSWORD: str = "postgres"
    # TEST_DATABASE_PORT: int = 5432
    # TEST_DATABASE_DB: str = "postgres"

    # FIRST SUPERUSER
    # FIRST_SUPERUSER_EMAIL: EmailStr
    # FIRST_SUPERUSER_PASSWORD: str


settings: Settings = Settings()  # type: ignore

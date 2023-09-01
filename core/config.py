import os
from pydantic import BaseSettings, PostgresDsn, validator, EmailStr, AnyHttpUrl
from typing import Any
import secrets
from enum import Enum
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())



class ModeEnum(str, Enum):
    development = "development"
    production = "production"
    testing = "testing"


class Settings(BaseSettings):
    MODE: ModeEnum = ModeEnum.development
    API_VERSION: str = "v1"
    API_V1_STR: str = f"/api/{API_VERSION}"
    PROJECT_NAME: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 1  # 1 hour
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 100  # 100 days
    OPENAI_API_KEY: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int | str
    DATABASE_NAME: str
    DATABASE_CELERY_NAME: str = "celery_schedule_jobs"
    REDIS_HOST: str
    REDIS_PORT: str
    DB_POOL_SIZE = 83
    WEB_CONCURRENCY = 9
    POOL_SIZE = max(DB_POOL_SIZE // WEB_CONCURRENCY, 5)
    ASYNC_DATABASE_URI: PostgresDsn | None

    @validator("ASYNC_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: str | None, values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("DATABASE_USER"),
            password=values.get("DATABASE_PASSWORD"),
            host=values.get("DATABASE_HOST"),
            port=str(values.get("DATABASE_PORT")),
            path=f"/{values.get('DATABASE_NAME') or ''}",
        )

    SYNC_CELERY_DATABASE_URI: str | None

    @validator("SYNC_CELERY_DATABASE_URI", pre=True)
    def assemble_celery_db_connection(
            cls, v: str | None, values: dict[str, Any]
    ) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="db+postgresql",
            user=values.get("DATABASE_USER"),
            password=values.get("DATABASE_PASSWORD"),
            host=values.get("DATABASE_HOST"),
            port=str(values.get("DATABASE_PORT")),
            path=f"/{values.get('DATABASE_CELERY_NAME') or ''}",
        )

    SYNC_CELERY_BEAT_DATABASE_URI: str | None

    @validator("SYNC_CELERY_BEAT_DATABASE_URI", pre=True)
    def assemble_celery_beat_db_connection(
            cls, v: str | None, values: dict[str, Any]
    ) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            user=values.get("DATABASE_USER"),
            password=values.get("DATABASE_PASSWORD"),
            host=values.get("DATABASE_HOST"),
            port=str(values.get("DATABASE_PORT")),
            path=f"/{values.get('DATABASE_CELERY_NAME') or ''}",
        )

    ASYNC_CELERY_BEAT_DATABASE_URI: str | None

    @validator("ASYNC_CELERY_BEAT_DATABASE_URI", pre=True)
    def assemble_async_celery_beat_db_connection(
            cls, v: str | None, values: dict[str, Any]
    ) -> Any:
        print(values)
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("DATABASE_USER"),
            password=values.get("DATABASE_PASSWORD"),
            host=values.get("DATABASE_HOST"),
            port=str(values.get("DATABASE_PORT")),
            path=f"/{values.get('DATABASE_CELERY_NAME') or ''}",
        )

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = os.path.expanduser("~/.env")


settings = Settings()

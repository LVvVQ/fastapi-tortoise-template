import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # App
    APP_NAME: str = os.environ.get("APP_NAME", "FastAPI App")

    # FrontEnd Application
    FRONTEND_HOST: str = os.environ.get("FRONTEND_HOST", "http://localhost:3000")

    # MySQL Database
    MYSQL_DSN: str = os.environ.get(
        "MYSQL_DSN", "mysql://root:123456@127.0.0.1:3306/fastapi_test"
    )


@lru_cache
def get_settings():
    return Settings()

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

    # Email
    MAIL_USERNAME: str = os.environ.get("MAIL_USERNAME", "")
    MAIL_PASSWORD: str = os.environ.get("MAIL_PASSWORD", "")
    MAIL_PORT: int = int(os.environ.get("MAIL_PORT", 465))
    MAIL_SERVER: str = os.environ.get("MAIL_SERVER", "smtp")
    MAIL_FROM: str = os.environ.get("MAIL_FROM", "lvvvq@qq.com")
    MAIL_FROM_NAME: str = os.environ.get("MAIL_FROM_NAME", APP_NAME)
    MAIL_STARTTLS: bool = bool(os.environ.get("MAIL_STARTTLS", False))
    MAIL_SSL_TLS: bool = bool(os.environ.get("MAIL_SSL_TLS", False))
    MAIL_DEBUG: bool = bool(os.environ.get("MAIL_DEBUG", False))


@lru_cache
def get_settings():
    return Settings()

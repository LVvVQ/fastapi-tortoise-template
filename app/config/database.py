from functools import partial

from tortoise.contrib.fastapi import RegisterTortoise

from app.config import settings

settings = settings.get_settings()

TORTOISE_ORM = {
    "connections": {"default": settings.MYSQL_DSN},
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


register_orm = partial(
    RegisterTortoise,
    config=TORTOISE_ORM,
    add_exception_handlers=True,
    use_tz=False,
    timezone="Asia/Shanghai",
)

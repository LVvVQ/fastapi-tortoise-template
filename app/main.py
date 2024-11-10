from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.config.database import register_orm
from app.routes import user


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    async with register_orm(app):
        yield


def create_app():
    app = FastAPI(lifespan=lifespan)
    app.include_router(user.user_router)
    return app


app = create_app()


@app.get("/")
async def root():
    return {"message": "Hi, I am LVvVQ. Awesome - Your setrup is done & working."}

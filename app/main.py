
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import os
from fastapi import FastAPI
# from app.config.database import init_db
from .routers.api import api_router
from .models.users import User
from fastapi.middleware.cors import CORSMiddleware
from .config.config import settings
from contextlib import asynccontextmanager
# from app.config.database import init_db



async def init_db():
    client = AsyncIOMotorClient(os.environ.get("MONGO_URL"))
    db_names = await client.list_database_names()
    print(f"----------------{db_names}")
    database = client[os.environ.get("MONGO_DB","FeIntel")]
    await init_beanie(database, document_models=[User])

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Startup event
#     await init_db()

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with MongoDB and Beanie"}


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            # See https://github.com/pydantic/pydantic/issues/7186 for reason of using rstrip
            str(origin).rstrip("/")
            for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
app.include_router(api_router, prefix=settings.API_V1_STR)

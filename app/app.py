# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
# Beanie
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
# My Dependencies
from core.config import settings
from api.api_v1.router import router
from models.user_model import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).auth
    
    await init_beanie(
        database=client,
        document_models=[
            User,
        ]
    )
    
    yield
    
    # Shutdown
    client.close
    
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f'{settings.API_V1_STR}/openapi.json',
    lifespan=lifespan
)
app.include_router(
    router,
    prefix=settings.API_V1_STR
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://127.0.0.1",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


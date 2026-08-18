from fastapi import FastAPI

from app.database import Base, engine
from app.models import User
from app.auth import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="JWT Authentication API")

app.include_router(router, prefix="/auth", tags=["Authentication"])

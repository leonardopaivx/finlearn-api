from fastapi import APIRouter
from app.api.v1.endpoints import user, auth

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])

from fastapi import APIRouter
from app.api.v1.endpoints import user, auth, talk, post

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])

api_router.include_router(talk.router, prefix="/talk", tags=["network"])
api_router.include_router(post.router, prefix="/post", tags=["network"])

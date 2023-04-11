from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.middleware.auth import authenticate_user_api_endpoints
from app.core.middleware.db import get_db
from app.core.middleware.error_handler import ErrorModel

from app.core.models import IdOut
from app.domain.social_media.models.post_model import (
    PostInputSchema,
    PostOutputSchema,
    PostSchema,
)
from app.domain.social_media.repositories import post_repository
from app.domain.user.entities.user import User


router = APIRouter()


@router.post("/create", status_code=201, response_model=IdOut)
def create_post(
    post_input: PostInputSchema,
    db: Session = Depends(get_db),
    _current_user: User = Depends(authenticate_user_api_endpoints),
):
    post = post_repository.create_post(db=db, input_post_data=post_input)

    return post

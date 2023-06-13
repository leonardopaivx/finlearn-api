from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.middleware.auth import authenticate_user_api_endpoints
from app.core.middleware.db import get_db
from app.core.middleware.error_handler import ErrorModel

from app.core.models import IdOut
from app.domain.social_media.models.post_model import (
    PostInputSchema,
    PostLikeInputSchema,
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
    """
    Cria uma publicação a partir de uma conversa.

    - Acesso: User
    """
    post = post_repository.create_post(db=db, input_post_data=post_input)

    return post


@router.get("", response_model=list[PostOutputSchema])
def get_post(
    db: Session = Depends(get_db),
    _current_user: User = Depends(authenticate_user_api_endpoints),
):
    """
    Retorna Todos os Posts do Banco.

    - Acesso: ALL
    """
    return post_repository.get_post(db=db)


@router.post("/like", status_code=201, response_model=IdOut)
def create_post_like(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user_api_endpoints),
):
    """
    Usuário autenticado realiza um like em um post.

    - Acesso: User
    """

    post_like_input = PostLikeInputSchema(user_id=current_user.id, post_id=post_id)
    post_like = post_repository.create_post_like(
        db=db, input_post_like_data=post_like_input
    )

    return post_like

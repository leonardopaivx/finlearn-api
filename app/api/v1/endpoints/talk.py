from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.middleware.auth import authenticate_user_api_endpoints
from app.core.middleware.db import get_db
from app.core.middleware.error_handler import ErrorModel

from app.core.models import IdOut
from app.domain.social_media.models.talk_model import (
    TalkInputSchema,
    TalkOutputSchema,
    TalkSchema,
)
from app.domain.social_media.repositories import talk_repository
from app.domain.user.entities.user import User


router = APIRouter()


@router.post("/create", status_code=201, response_model=IdOut)
def create_talk(
    talk_input: TalkInputSchema,
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user_api_endpoints),
):
    """
    Cria uma conversa a partir de um usuário autenticado.

    - Acesso: ADMIN
    """
    talk = talk_repository.create_talk(
        db=db, title=talk_input.title, user_id=current_user.id
    )

    return talk


@router.get("", response_model=list[TalkOutputSchema])
def get_talk(
    db: Session = Depends(get_db),
    _current_user: User = Depends(authenticate_user_api_endpoints),
):
    """
    Retorna Todas as Conversas do Banco.

    - Acesso: ALL
    """
    return talk_repository.get_talk(db=db)

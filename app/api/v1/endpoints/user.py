from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.middleware.db import get_db
from app.core.middleware.error_handler import ErrorModel

from app.core.models import IdOut
from app.domain.user.models.user_model import UserInputSchema
from app.domain.user.repositories import user_repository
from app.providers import hash_provider
from app.domain.user.entities.user import User
from app.domain.social_media.models.talk_model import TalkOutputSchema
from app.core.middleware.auth import authenticate_user_api_endpoints

router = APIRouter()


@router.post("/create", status_code=201, response_model=IdOut)
def create_user(
    user_input: UserInputSchema,
    db: Session = Depends(get_db),
):
    """
    Registra um usuário.

    - Acesso: ALL
    """
    user_found = user_repository.get_by_email(db=db, email=user_input.email)

    if user_found:
        raise ErrorModel.bad_request("E-mail já cadastrado")

    user_input.password = hash_provider.generate_hash(user_input.password)

    user = user_repository.create_user(db=db, input_user_data=user_input)

    return user


@router.get("/me/talks", response_model=list[TalkOutputSchema])
def get_user_talks(
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user_api_endpoints),
):
    """
    Retorna Todas as Conversas de um usuário autenticado.

    - Acesso: ALL
    """
    return user_repository.get_user_talks(db=db, input_id=current_user.id)

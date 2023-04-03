from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app.core.middleware.error_handler import ErrorModel
from app.domain.user.repositories import user_repository
from app.providers.token_provider import verify_acess_token
from jose import JWTError

from app.core.middleware.db import get_db

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")


def authenticate_user_api_endpoints(
    token: str = Depends(oauth2_schema), db: Session = Depends(get_db)
):
    try:
        user_id = int(verify_acess_token(token))
    except (JWTError):
        raise ErrorModel.unauthorized(note="Token Inválido")

    if not user_id:
        raise ErrorModel.unauthorized(note="Token Inválido")

    user = user_repository.get_user_by_id(db=db, input_id=user_id)

    if not user:
        raise ErrorModel.unauthorized(note="Token Inválido")

    return user

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.middleware.db import get_db
from app.core.middleware.error_handler import ErrorModel
from app.domain.user.entities.user import User
from app.domain.user.models.user_model import (
    LoginInputSchema,
    LoginSuccessSchema,
    UserOutputSchema,
)
from app.domain.user.repositories import user_repository
from app.providers import hash_provider, token_provider
from app.core.middleware.auth import authenticate_user_api_endpoints


router = APIRouter()


@router.post("/login")
def login(login_data: LoginInputSchema, db: Session = Depends(get_db)):
    """
    Rota para retornar um access_token.

    - Acesso: ALL
    """
    email = login_data.email
    password = login_data.password

    user = user_repository.get_by_email(db=db, email=email)

    if not user:
        raise ErrorModel.bad_request(note="Usuário ou senha estão incorretos!")

    valid_pass = hash_provider.verify_hash(password, user.password)

    if not valid_pass:
        raise ErrorModel.bad_request(note="Usuário ou senha estão incorretos!")

    token = token_provider.create_access_token({"sub": str(user.id)})

    return LoginSuccessSchema(user=user, access_token=token)


@router.get("/me", response_model=UserOutputSchema)
def get_me(current_user: User = Depends(authenticate_user_api_endpoints)):
    """
    Retorna informações do usuário autenticado.

    - Acesso: ALL
    """
    print(current_user)
    return UserOutputSchema(
        id=current_user.id,
        name=current_user.name,
        telephone=current_user.telephone,
        email=current_user.email,
        role=current_user.role,
    )

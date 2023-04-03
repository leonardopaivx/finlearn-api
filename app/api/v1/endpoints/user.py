from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.middleware.db import get_db
from app.core.middleware.error_handler import ErrorModel

from app.core.models import IdOut
from app.domain.user.models.user_model import UserInputSchema
from app.domain.user.repositories import user_repository
from app.providers import hash_provider


router = APIRouter()


@router.post("/create", status_code=201, response_model=IdOut)
def create_user(
    user_input: UserInputSchema,
    db: Session = Depends(get_db),
):
    user_found = user_repository.get_by_email(db=db, email=user_input.email)

    if user_found:
        raise ErrorModel.bad_request("E-mail já cadastrado")

    user_input.password = hash_provider.generate_hash(user_input.password)

    user = user_repository.create_user(db=db, input_user_data=user_input)

    return user

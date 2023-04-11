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
    _current_user: User = Depends(authenticate_user_api_endpoints),
):
    talk = talk_repository.create_talk(db=db, input_talk_data=talk_input)

    return talk

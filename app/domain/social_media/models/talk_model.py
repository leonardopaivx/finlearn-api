# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from pydantic import BaseModel
from app.domain.user.entities.user import UserRoleList
from app.domain.social_media.models.post_model import PostOutputSchema
from app.domain.user.models.user_model import BasicUserSchema


class TalkSchema(BaseModel):
    id: int
    title: str
    user_id: int


class TalkInputSchema(BaseModel):
    title: str
    # user_id: int


class TalkOutputSchema(BaseModel):
    id: int
    title: str
    user: BasicUserSchema | None
    post_data: list[PostOutputSchema] | None

    class Config:
        orm_mode = True

# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from pydantic import BaseModel
from app.domain.user.entities.user import UserRoleList


class TalkSchema(BaseModel):
    id: int
    title: str
    user_id: int


class TalkInputSchema(BaseModel):
    title: str
    user_id: int


class TalkOutputSchema(BaseModel):
    id: int
    title: str
    user_id: int

    class Config:
        orm_mode = True

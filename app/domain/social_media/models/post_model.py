# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from pydantic import BaseModel
from app.domain.user.entities.user import UserRoleList


class PostSchema(BaseModel):
    id: int
    base_text: str
    talk_id: int


class PostInputSchema(BaseModel):
    base_text: str
    talk_id: int


class PostOutputSchema(BaseModel):
    id: int
    base_text: str
    talk_id: int

    class Config:
        orm_mode = True

class PostLikeSchema(BaseModel):
    id: int
    user_id: int
    post_id: int

class PostLikeInputSchema(BaseModel):
    user_id: int
    post_id: int

class PostLikeOutputSchema(BaseModel):
    id: int
    user_id: int
    post_id: int
    
    class Config:
        orm_mode = True
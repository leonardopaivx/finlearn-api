# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from pydantic import BaseModel
from app.domain.user.entities.user import UserRoleList
from app.domain.user.models.user_model import BasicUserSchema


class PostSchema(BaseModel):
    id: int
    base_text: str
    talk_id: int


class PostInputSchema(BaseModel):
    base_text: str
    talk_id: int


class LikeSchema(BaseModel):
    user_id: int
    class Config:
        orm_mode = True



class PostOutputSchema(BaseModel):
    id: int
    base_text: str
    user: BasicUserSchema
    likes_data : list[LikeSchema] | None

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
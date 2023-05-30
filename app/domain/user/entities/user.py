from enum import Enum
import sqlalchemy as sa
from sqlalchemy.types import VARCHAR, TypeDecorator
from sqlalchemy.orm import relationship
from app.core.entities.base import Base
from app.core.entities.audits import Audits
from app.domain.social_media.entities.post import Post, PostLike

from app.domain.social_media.entities.talk import Talk


class UserRoleList(str, Enum):
    ADMIN = "ADMIN"
    NORMAL_USER = "NORMAL_USER"
    SPECIALIST = "SPECIALIST"


class RolesDB(TypeDecorator):
    impl = VARCHAR(255)

    cache_ok = True

    def process_bind_param(self, value, dialect):
        if isinstance(value, UserRoleList):
            return value.value
        elif isinstance(value, str):
            return value
        raise ValueError("Invalid value for RolesDB")

    def process_result_value(self, value, dialect):
        return UserRoleList(value)


class User(Base, Audits):
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String)
    name = sa.Column(sa.String)
    role = sa.Column(RolesDB(UserRoleList))
    telephone = sa.Column(sa.String, nullable=True)
    password = sa.Column(sa.String)

    talk_data: list["Talk"] = relationship("Talk", backref="user")
    post_data : list["Post"] = relationship("Post", backref="user")
    likes_data : list["PostLike"] = relationship("PostLike", backref="user")
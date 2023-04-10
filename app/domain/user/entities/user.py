from enum import Enum
import sqlalchemy as sa
from sqlalchemy.types import VARCHAR, TypeDecorator
from app.core.entities.base import Base
from app.core.entities.audits import Audits


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

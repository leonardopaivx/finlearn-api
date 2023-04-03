import sqlalchemy as sa
from app.core.entities.base import Base
from app.core.entities.audits import Audits


class User(Base, Audits):
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String)
    name = sa.Column(sa.String)
    telephone = sa.Column(sa.String, nullable=True)
    password = sa.Column(sa.String)

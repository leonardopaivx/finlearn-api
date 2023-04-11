import sqlalchemy as sa
from sqlalchemy.types import VARCHAR
from app.core.entities.base import Base
from app.core.entities.audits import Audits


class Post(Base, Audits):
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    base_text: str = sa.Column(VARCHAR(255))

    talk_id: int = sa.Column(sa.ForeignKey("talk.id", ondelete="SET NULL"))

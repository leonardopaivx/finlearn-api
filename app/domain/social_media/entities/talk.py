import sqlalchemy as sa
from sqlalchemy.types import VARCHAR
from sqlalchemy.orm import relationship
from app.core.entities.base import Base
from app.core.entities.audits import Audits

from app.domain.social_media.entities.post import Post


class Talk(Base, Audits):
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)

    user_id: int = sa.Column(sa.ForeignKey("user.id", ondelete="SET NULL"))

    post_data: list["Post"] = relationship("Post", backref="talk")

    user = relationship("User", back_populates="talk_data")
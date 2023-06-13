import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.types import VARCHAR
from app.core.entities.base import Base
from app.core.entities.audits import Audits


class Post(Base, Audits):
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    base_text: str = sa.Column(VARCHAR(255))

    talk_id: int = sa.Column(sa.ForeignKey("talk.id", ondelete="SET NULL"))
    user_id: int = sa.Column(sa.ForeignKey("user.id", ondelete="SET NULL"))
    likes_data : list["PostLike"] = relationship("PostLike", backref="post")

    user = relationship("User", back_populates="post_data")


class PostLike(Base, Audits):
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    user_id: int = sa.Column(sa.ForeignKey("user.id", ondelete="SET NULL"))
    post_id: int = sa.Column(sa.ForeignKey("post.id", ondelete="SET NULL"))

    user = relationship("User", back_populates="likes_data")
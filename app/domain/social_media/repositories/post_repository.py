import sqlalchemy as sa
from sqlalchemy.orm import Session
from app.domain.social_media.entities.post import Post
from app.domain.social_media.models.post_model import (
    PostInputSchema,
    PostOutputSchema,
    PostSchema,
)


def exists(db: Session, input_id: int) -> bool:
    stmt = sa.select(Post).where(Post.id == input_id)
    stmt_result = db.execute(stmt)
    return stmt_result.scalar() is not None


def create_post(db: Session, input_post_data: PostInputSchema) -> Post:
    post = Post(
        base_text=input_post_data.base_text,
        talk_id=input_post_data.talk_id,
    )

    db.add(post)
    db.commit()

    return post


def get_post(db: Session) -> list[Post]:
    stmt = sa.select(Post)
    stmt_result = db.execute(stmt)
    return stmt_result.scalars().all()


def get_post_by_id(db: Session, input_id: int) -> Post:
    stmt = sa.select(Post).where(Post.id == input_id)
    stmt_result = db.execute(stmt)
    return stmt_result.scalar()


def get_post_by_talk(db: Session, input_id: int) -> list[Post]:
    stmt = sa.select(Post).where(Post.talk_id == input_id)
    stmt_result = db.execute(stmt)
    return stmt_result.scalars().all()

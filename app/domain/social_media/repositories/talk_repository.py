import sqlalchemy as sa
from sqlalchemy.orm import Session
from app.domain.social_media.entities.talk import Talk
from app.domain.social_media.models.talk_model import (
    TalkInputSchema,
    TalkOutputSchema,
    TalkSchema,
)


def exists(db: Session, input_id: int) -> bool:
    stmt = sa.select(Talk).where(Talk.id == input_id)
    stmt_result = db.execute(stmt)
    return stmt_result.scalar() is not None


def create_talk(db: Session, title: str, user_id: int) -> Talk:
    talk = Talk(
        title=title,
        user_id=user_id,
    )

    db.add(talk)
    db.commit()

    return talk


def get_talk(db: Session) -> list[Talk]:
    stmt = sa.select(Talk)
    stmt_result = db.execute(stmt)
    return stmt_result.scalars().all()


def get_talk_by_id(db: Session, input_id: int) -> Talk:
    stmt = sa.select(Talk).where(Talk.id == input_id)
    stmt_result = db.execute(stmt)
    return stmt_result.scalar()

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


def create_talk(db: Session, input_talk_data: TalkInputSchema) -> Talk:
    talk = Talk(
        title=input_talk_data.title,
        user_id=input_talk_data.user_id,
    )

    db.add(talk)
    db.commit()

    return talk

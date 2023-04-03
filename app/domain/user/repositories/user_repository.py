import sqlalchemy as sa
from sqlalchemy.orm import Session
from app.domain.user.entities.user import User
from app.domain.user.models.user_model import LoginInputSchema, UserInputSchema


def exists(db: Session, input_id: int) -> bool:
    stmt = sa.select(User).where(User.id == input_id)
    stmt_result = db.execute(stmt)
    return stmt_result.scalar() is not None


def create_user(db: Session, input_user_data: UserInputSchema) -> User:
    user = User(
        email=input_user_data.email,
        name=input_user_data.name,
        telephone=input_user_data.telephone,
        password=input_user_data.password,
    )

    db.add(user)
    db.commit()

    return user


def get_by_email(db: Session, email: str) -> User:
    stmt = sa.select(User).where(User.email == email)
    stmt_result = db.execute(stmt)
    return stmt_result.scalar()


def get_user_by_id(db: Session, input_id: int) -> User:
    stmt = sa.select(User).where(User.id == input_id)
    stmt_result = db.execute(stmt)
    return stmt_result.scalar()

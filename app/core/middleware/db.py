from app.config.database import SessionLocal


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        if db is not None:
            db.close()

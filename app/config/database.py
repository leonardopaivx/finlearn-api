from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from app.config.settings import setting

DATABASE_URL = setting.DB_URL


class DBSettings:
    def __init__(self, url: str, **kwargs) -> None:
        self.url_db = url
        self.engine = create_engine(self.url_db, future=True, **kwargs)

        if "sqlite://" in self.url_db:
            # trigger checagens de foreign key do sqlite
            @event.listens_for(self.engine, "connect")
            def set_sqlite_pragma(connection, *_):
                cursor = connection.cursor()
                cursor.execute("PRAGMA foreign_keys=ON")
                cursor.close()

        self.session_local = sessionmaker(bind=self.engine, future=True)


settings_db = DBSettings(DATABASE_URL)

engine = settings_db.engine
SessionLocal = settings_db.session_local

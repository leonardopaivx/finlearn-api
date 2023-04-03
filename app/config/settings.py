from pydantic import BaseSettings


class Settings(BaseSettings):

    DB_URL: str | None

    TEST_ENV: bool = False

    SECRET_KEY: str | None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


setting = Settings()

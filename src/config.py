import os

from pydantic_settings  import BaseSettings # type: ignore

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
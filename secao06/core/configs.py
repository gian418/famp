from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/faculdade"
    DBBaseModel: ClassVar  = declarative_base()

    """
    Para gerar um Secret Key
    import secrets
    token: str = secrets.token_urlsafe(32)
    """
    JWT_SECRET_KEY: str = "WcugK6jid2G5AAeQravpP30CZHhFB7mh0sxFqGLjl5s"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
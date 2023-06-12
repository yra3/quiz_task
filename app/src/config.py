from pydantic import BaseSettings, PostgresDsn


class Config(BaseSettings):
    DATABASE_URL: PostgresDsn = "postgresql://postgres:postgres@localhost:5432/"
    SITE_DOMAIN: str = "localhost"
    DEBUG: bool = True
    APP_VERSION: str = "1"


settings = Config()

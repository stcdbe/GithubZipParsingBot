from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_API_TOKEN: str

    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_DB: str

    model_config = SettingsConfigDict(env_file='.env', case_sensitive=True)


settings = Settings()

REDIS_URL = f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}'

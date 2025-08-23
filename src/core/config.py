from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings

from .helpers import load_environment


class BotSettings(BaseSettings, env_prefix="bot_"):
    token: str


class Settings(BaseSettings):
    # Bot
    bot: BotSettings = Field(default_factory=BotSettings)


@lru_cache
def get_settings() -> Settings:
    load_environment()
    return Settings()


settings = get_settings()

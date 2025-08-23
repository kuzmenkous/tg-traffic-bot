from functools import lru_cache

from pydantic import Field
from pydantic.networks import AmqpDsn, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings

from .helpers import load_environment
from .pydantic_types import TimezoneInfo


class BotSettings(BaseSettings, env_prefix="bot_"):
    token: str


class DBSettings(BaseSettings, env_prefix="db_"):
    name: str
    user: str
    password: str
    host: str
    port: int

    @property
    def url(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql+psycopg",
                username=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                path=f"{self.name}",
            )
        )


class RedisSettings(BaseSettings, env_prefix="redis_"):
    host: str
    port: int
    password: str

    @property
    def url(self) -> RedisDsn:
        return RedisDsn.build(
            scheme="redis",
            host=self.host,
            port=self.port,
            password=self.password,
        )


class RabbitMQSettings(BaseSettings, env_prefix="rabbitmq_"):
    user: str
    password: str
    host: str
    port: int

    @property
    def url(self) -> AmqpDsn:
        return AmqpDsn.build(
            scheme="amqp",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )


class Settings(BaseSettings):
    # Bot
    bot: BotSettings = Field(default_factory=BotSettings)
    # Database
    db: DBSettings = Field(default_factory=DBSettings)
    # Redis
    redis: RedisSettings = Field(default_factory=RedisSettings)
    # RabbitMQ
    rabbitmq: RabbitMQSettings = Field(default_factory=RabbitMQSettings)

    # Timezone
    timezone: TimezoneInfo


@lru_cache
def get_settings() -> Settings:
    load_environment()
    return Settings()


settings = get_settings()

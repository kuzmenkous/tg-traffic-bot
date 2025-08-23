from aiogram import Bot, Dispatcher, enums
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage
from redis import asyncio as aioredis

from .core.config import settings

# Telegram Bot
bot = Bot(
    token=settings.bot.token,
    default=DefaultBotProperties(parse_mode=enums.ParseMode.MARKDOWN),
)

# Storage
redis = aioredis.from_url(settings.redis.url)  # type: ignore[no-untyped-call]
redis_storage = RedisStorage(redis=redis)

# Dispatcher
dp = Dispatcher(bot=bot, storage=redis_storage)

import asyncio

from .loader import bot, dp, redis_storage
from .routers.main import router as main_router


async def on_shutdown() -> None:
    await bot.close()
    await redis_storage.close()


if __name__ == "__main__":
    for router in (main_router,):
        dp.include_router(router)
    asyncio.run(dp.start_polling(bot, on_shutdown=on_shutdown))

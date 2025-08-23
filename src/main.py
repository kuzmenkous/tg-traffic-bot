import asyncio

from aiogram import Router

from .loader import bot, dp, redis_storage


async def on_shutdown() -> None:
    await bot.close()
    await redis_storage.close()


# Include routers
routers: list[Router] = []


if __name__ == "__main__":
    for router in routers:
        dp.include_router(router)
    asyncio.run(dp.start_polling(bot, on_shutdown=on_shutdown))

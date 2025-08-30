import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from ..loader import bot as main_bot
from ..utils.markdown import escape_markdown

log = logging.getLogger(__name__)


class BotsManager:
    def __init__(self):
        self.tasks: dict[str, asyncio.Task] = {}
        self.dispatchers: dict[str, Dispatcher] = {}
        self.bots: dict[str, Bot] = {}

    def setup_dispatcher(self, dp: Dispatcher):
        @dp.message(Command("start"))
        async def start_handler(message: types.Message):
            bot = message.bot
            me = await bot.me()
            await message.answer(f"Hello from bot @{me.username}!")

        @dp.message(Command("help"))
        async def help_handler(message: types.Message):
            await message.answer("This is a help message.")

        @dp.message(Command("my_id"))
        async def my_id_handler(message: types.Message):
            await message.answer(f"Your ID is {message.from_user.id}")

        @dp.my_chat_member()
        async def chat_member_handler(event: types.ChatMemberUpdated):
            chat = event.chat
            new_status = event.new_chat_member.status
            old_status = event.old_chat_member.status

            if chat.type == "channel":
                if (
                    old_status in ("left", "kicked")
                    and new_status == "administrator"
                ):
                    bot = await event.bot.get_me()
                    await main_bot.send_message(
                        event.from_user.id,
                        escape_markdown(
                            f"Бот @{bot.username} успешно был добавлен в канал"
                            f" *{chat.title}* и назначен администратором.\n"
                            "Теперь вы и другие админы можете им пользоваться"
                            " (если админы имеют соответствующий доступ)"
                        ),
                    )
                elif new_status == "left":
                    bot = await event.bot.get_me()
                    await main_bot.send_message(
                        event.from_user.id,
                        escape_markdown(
                            f"Бот @{bot.username} был удален из канала"
                            f" *{chat.title}* или у него отозваны права"
                            " администратора.\n"
                            "Он больше не сможет помогать вам в этом канале."
                        ),
                    )

    async def start_bot(self, token: str):
        if token not in self.tasks:
            bot = Bot(token)
            dp = Dispatcher()
            self.setup_dispatcher(dp)

            self.bots[token] = bot
            self.dispatchers[token] = dp

            task = asyncio.create_task(dp.start_polling(bot))
            self.tasks[token] = task
        else:
            self.stop_bot(token)

    async def stop_bot(self, token: str):
        if token in self.tasks:
            # cancel polling
            self.tasks[token].cancel()
            if not self.tasks[token].cancelled():
                pass

            # close bot session
            await self.bots[token].session.close()

            # cleanup
            del self.tasks[token]
            del self.dispatchers[token]
            del self.bots[token]

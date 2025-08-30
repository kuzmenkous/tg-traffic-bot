from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from ..core.config import settings
from ..utils.markdown import escape_markdown

router = Router(name="main_router")


@router.message(Command("start"))
async def start_command_handler(message: Message) -> None:
    if message.from_user is not None:
        user_id = message.from_user.id
        await message.answer(f"Your Telegram ID is {user_id}")
    text = (
        f"*{settings.bot.name}* — инновационный сервис для управления приветственными сообщениями в приватных каналах.\n\n"
        f"С *{settings.bot.name}* вы получаете:\n\n"
        f"🔹 *Умный приветственный бот* — Фильтрует заявки и отсеивает лишних\n"
        f"— Формирует базу подписчиков\n"
        f"— Делает рассылки прямо в личные сообщения\n"
        f"— Сохраняет ваш трафик и анализирует эффективность закупок\n\n"
        f"🔹 *Контроль и безопасность дохода* — *{settings.bot.name}* — это не просто бот, а ваш"
        f" персональный щит и инструмент управления прибылью.\n"
        f"— Защищает канал, автоматизирует коммуникацию и помогает выстраивать доверительные отношения с аудиторией, "
        f"сохраняя каждый контакт и максимизируя доход."
    )
    await message.answer(escape_markdown(text))

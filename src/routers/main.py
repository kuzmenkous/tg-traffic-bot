from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="main_router")


@router.message(Command("start"))
async def start_command_handler(message: Message) -> None:
    if message.from_user is not None:
        user_id = message.from_user.id
        await message.answer(f"Your Telegram ID is {user_id}")

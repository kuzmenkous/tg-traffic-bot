from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession

from src.core.config import settings
from src.enums.user import UserRole
from src.models.user import UserModel


async def insert_first_rows_with_async_connection(
    async_connection: AsyncConnection,
) -> None:
    session = AsyncSession(async_connection)
    await create_first_rows(session)
    await session.flush()


async def create_first_rows(session: AsyncSession) -> None:
    user_model = UserModel(
        tg_id=settings.bot.admin_id, role=UserRole.MAIN_ADMIN
    )
    session.add(user_model)
    await session.flush()

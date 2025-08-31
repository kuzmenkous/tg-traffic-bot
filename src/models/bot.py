from typing import Annotated, Optional

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..core.db.base import BaseModel
from ..core.db.mixins import TgIdMixin
from ..enums.bot import BotLanguage, BotStatus


class BotModel(BaseModel):
    __tablename__ = "bots"

    name: Mapped[str]
    token: Mapped[str] = mapped_column(unique=True, index=True)
    status: Mapped[BotStatus] = mapped_column(
        server_default=BotStatus.STARTED.name
    )
    language: Mapped[BotLanguage] = mapped_column(
        server_default=BotLanguage.EN.name
    )
    support_chat_tg_id: Mapped[int | None] = mapped_column(BigInteger)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )

    channel: Mapped[Optional["BotChannelModel"]] = relationship()

    def __str__(self) -> str:
        return f"Bot: {self.name} - {self.token}"


BotId = Annotated[
    int,
    mapped_column(
        ForeignKey("bots.id", ondelete="CASCADE", onupdate="CASCADE")
    ),
]


class UniqueBotIdMixin:
    bot_id: Mapped[BotId] = mapped_column(unique=True)


class BotChannelModel(TgIdMixin, UniqueBotIdMixin, BaseModel):
    __tablename__ = "bot_channels"

    name: Mapped[str]

    def __str__(self) -> str:
        return f"BotChannel: {self.name} - {self.tg_id}"

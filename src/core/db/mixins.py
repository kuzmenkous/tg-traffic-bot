from sqlalchemy import BigInteger, true
from sqlalchemy.orm import Mapped, mapped_column


class IsActiveMixin:
    is_active: Mapped[bool] = mapped_column(server_default=true())


class TgIdMixin:
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)

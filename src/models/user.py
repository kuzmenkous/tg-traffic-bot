from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from ..core.db.base import BaseModel
from ..enums.user import UserRole


class UserModel(BaseModel):
    __tablename__ = "users"

    tg_id: Mapped[int] = mapped_column(BIGINT, unique=True, index=True)
    role: Mapped[UserRole]

    def __str__(self) -> str:
        return f"User: {self.tg_id}, role: {self.role}"

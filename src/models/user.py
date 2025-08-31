from sqlalchemy.orm import Mapped

from ..core.db.base import BaseModel
from ..core.db.mixins import TgIdMixin
from ..enums.user import UserRole


class UserModel(TgIdMixin, BaseModel):
    __tablename__ = "users"

    role: Mapped[UserRole]

    def __str__(self) -> str:
        return f"User: {self.tg_id}, role: {self.role}"

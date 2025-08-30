from enum import StrEnum, auto, unique


@unique
class UserRole(StrEnum):
    USER = auto()
    ADMIN = auto()
    MAIN_ADMIN = auto()

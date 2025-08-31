from enum import StrEnum, auto, unique


@unique
class BotStatus(StrEnum):
    STARTED = auto()
    STOPPED = auto()


@unique
class BotLanguage(StrEnum):
    RU = auto()
    EN = auto()
    TR = auto()
    KA = auto()

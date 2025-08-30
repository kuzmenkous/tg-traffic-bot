from enum import StrEnum, auto, unique


@unique
class BotStatus(StrEnum):
    STARTED = auto()
    STOPPED = auto()

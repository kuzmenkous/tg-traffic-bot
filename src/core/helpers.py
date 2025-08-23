from dotenv import load_dotenv

from ..exceptions.helpers import (
    DotenvListException,
    DotenvLoadException,
    DotenvStrokeException,
)

DOTENV_FILE = ".env"


class DotenvListHelper:
    """Class for getting a list from a string value in a .env file."""

    @staticmethod
    def _assemble_list(value: str) -> list[str]:
        try:
            return [v.strip() for v in value.strip("[]").split(",") if v]
        except ValueError:
            raise DotenvListException

    @staticmethod
    def _assemble_stroke(value: str) -> list[str]:
        try:
            return [v.strip() for v in value.split(",") if v]
        except ValueError:
            raise DotenvStrokeException

    @classmethod
    def get_list_from_value(cls, value: str) -> list[str]:
        if value.startswith("[") and value.endswith("]"):
            return cls._assemble_list(value)
        return cls._assemble_stroke(value)


def load_environment() -> None:
    try:
        load_dotenv(dotenv_path=DOTENV_FILE)
    except OSError:
        raise DotenvLoadException(DOTENV_FILE)

from .base import BaseCustomException


class DotenvBaseException(BaseCustomException):
    pass


class DotenvListException(DotenvBaseException):
    def __init__(self) -> None:
        super().__init__(
            message="Could not parse list from environment variable"
        )


class DotenvStrokeException(DotenvBaseException):
    def __init__(self) -> None:
        super().__init__(
            message="Could not parse stroke from environment variable"
        )


class DotenvLoadException(DotenvBaseException):
    def __init__(self, filepath: str) -> None:
        super().__init__(
            message=f"Could not load .env file from path: {filepath}"
        )

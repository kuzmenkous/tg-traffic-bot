from .base import BaseCustomException


class DotenvBaseException(BaseCustomException):
    pass


class DotenvListException(DotenvBaseException):
    def __init__(self):
        super().__init__(
            message="Could not parse list from environment variable"
        )


class DotenvStrokeException(DotenvBaseException):
    def __init__(self):
        super().__init__(
            message="Could not parse stroke from environment variable"
        )


class DotenvLoadException(DotenvBaseException):
    def __init__(self, filepath: str):
        super().__init__(
            message=f"Could not load .env file from path: {filepath}"
        )

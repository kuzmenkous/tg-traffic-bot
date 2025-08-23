class BaseCustomException(Exception):
    error: str | None = None

    def __init__(self, message: str | None = None):
        if not message:
            message = self.error
        self.message = message
        super().__init__(message)

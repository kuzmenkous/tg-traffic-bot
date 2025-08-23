from .unitofwork import UnitOfWork


class BaseService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, Self

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

from ..db.session import session_factory


class AbstractUnitOfWork(ABC):
    @abstractmethod
    async def __aenter__(self) -> Self:
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args) -> None:  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def flush(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def add(self, instance: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    async def add_all(self, instances: Iterable[Any]) -> None:
        raise NotImplementedError


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self) -> None:
        self._session_factory = session_factory

    async def __aenter__(self) -> Self:
        self._session: AsyncSession = self._session_factory()

        # Initialize repositories

        return self

    async def __aexit__(self, *args) -> None:  # type: ignore[no-untyped-def]
        await self.rollback()
        await self._session.close()

    async def commit(self) -> None:
        await self._session.commit()

    async def flush(self) -> None:
        await self._session.flush()

    async def rollback(self) -> None:
        await self._session.rollback()

    async def add(self, instance: Any) -> None:
        self._session.add(instance)

    async def add_all(self, instances: Iterable[Any]) -> None:
        self._session.add_all(instances)

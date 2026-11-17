from abc import ABC, abstractmethod


class BaseEntity(ABC):
    """Абстрактный базовый класс для сущностей магазина."""

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        pass
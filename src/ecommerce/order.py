from ecommerce.base import BaseEntity
from ecommerce.product import Product


class Order(BaseEntity):
    """Представляет заказ одного товара."""

    def __init__(self, product: Product, quantity: int) -> None:
        """Инициализирует заказ."""
        if not isinstance(product, Product):
            raise TypeError("В заказе должен быть объект класса Product")

        if quantity <= 0:
            raise ValueError("Количество товара должно быть положительным")

        if quantity > product.quantity:
            raise ValueError("Недостаточно товара на складе")

        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity

    def __str__(self) -> str:
        """Возвращает информацию о заказе."""
        return (
            f"Заказ: {self.product.name}, "
            f"количество: {self.quantity} шт., "
            f"итого: {self.total_cost} руб."
        )
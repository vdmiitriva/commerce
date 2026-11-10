import pytest

from ecommerce.base import BaseEntity
from ecommerce.order import Order
from ecommerce.product import Product


def test_order_init():
    product = Product("Samsung", "Смартфон", 1000.0, 5)
    order = Order(product, 2)

    assert order.product is product
    assert order.quantity == 2
    assert order.total_cost == 2000.0


def test_order_str():
    product = Product("Samsung", "Смартфон", 1000.0, 5)
    order = Order(product, 2)

    assert str(order) == "Заказ: Samsung, количество: 2 шт., итого: 2000.0 руб."


def test_order_inherits_base_entity():
    product = Product("Samsung", "Смартфон", 1000.0, 5)
    order = Order(product, 2)

    assert isinstance(order, BaseEntity)


def test_order_invalid_product():
    with pytest.raises(TypeError):
        Order("Samsung", 2)


def test_order_invalid_quantity():
    product = Product("Samsung", "Смартфон", 1000.0, 5)

    with pytest.raises(ValueError):
        Order(product, 0)


def test_order_quantity_exceeds_stock():
    product = Product("Samsung", "Смартфон", 1000.0, 2)

    with pytest.raises(ValueError):
        Order(product, 3)
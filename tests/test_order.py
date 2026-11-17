import pytest

from ecommerce.base import BaseEntity
from ecommerce.exceptions import ZeroQuantityError
from ecommerce.order import Order, create_order
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

    with pytest.raises(ZeroQuantityError):
        Order(product, 0)


def test_order_quantity_exceeds_stock():
    product = Product("Samsung", "Смартфон", 1000.0, 2)

    with pytest.raises(ValueError):
        Order(product, 3)


def test_create_order_success(capsys):
    product = Product("Samsung", "Смартфон", 1000.0, 5)

    order = create_order(product, 2)

    captured = capsys.readouterr()

    assert isinstance(order, Order)
    assert order.total_cost == 2000.0
    assert "успешно добавлен в заказ" in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_create_order_zero_quantity(capsys):
    product = Product("Samsung", "Смартфон", 1000.0, 5)

    order = create_order(product, 0)

    captured = capsys.readouterr()

    assert order is None
    assert "Товар с нулевым количеством не может быть добавлен" in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_create_order_invalid_product(capsys):
    with pytest.raises(TypeError):
        create_order("Samsung", 2)

    captured = capsys.readouterr()

    assert "Обработка добавления товара завершена" in captured.out


def test_order_negative_quantity():
    product = Product("Samsung", "Смартфон", 1000.0, 5)

    with pytest.raises(
        ValueError,
        match="Количество товара должно быть положительным",
    ):
        Order(product, -1)

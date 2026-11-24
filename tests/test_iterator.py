import pytest

from ecommerce.category import Category
from ecommerce.iterator import CategoryIterator
from ecommerce.product import Product


def test_category_iterator_init() -> None:
    """Проверяет инициализацию итератора."""
    product = Product("Samsung", "Смартфон", 80000.0, 5)
    category = Category("Смартфоны", "Телефоны", [product])

    iterator = CategoryIterator(category)

    assert iterator.products == [product]
    assert iterator.index == 0


def test_category_iterator_returns_products() -> None:
    """Проверяет последовательное получение товаров."""
    product1 = Product("Samsung", "Смартфон", 80000.0, 5)
    product2 = Product("iPhone", "Смартфон", 100000.0, 3)
    category = Category("Смартфоны", "Телефоны", [product1, product2])

    iterator = CategoryIterator(category)

    assert iter(iterator) is iterator
    assert next(iterator) is product1
    assert next(iterator) is product2


def test_category_iterator_stops() -> None:
    """Проверяет остановку итерации после последнего товара."""
    product = Product("Samsung", "Смартфон", 80000.0, 5)
    category = Category("Смартфоны", "Телефоны", [product])

    iterator = CategoryIterator(category)

    next(iterator)

    with pytest.raises(StopIteration):
        next(iterator)


def test_category_iterator_empty_category() -> None:
    """Проверяет итерацию по пустой категории."""
    category = Category("Смартфоны", "Телефоны", [])
    iterator = CategoryIterator(category)

    with pytest.raises(StopIteration):
        next(iterator)

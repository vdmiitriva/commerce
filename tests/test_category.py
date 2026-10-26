from ecommerce.category import Category
from ecommerce.product import Product


def test_category_init():
    product = Product("Samsung", "Смартфон", 1000.0, 2)
    category = Category("Телефоны", "Мобильные устройства", [product])

    assert category.name == "Телефоны"
    assert category.description == "Мобильные устройства"
    assert category.products == [product]


def test_category_counters():
    initial_categories = Category.category_count
    initial_products = Category.product_count

    product1 = Product("Samsung", "Смартфон", 1000.0, 2)
    product2 = Product("Apple", "Смартфон", 2000.0, 3)

    Category("Телефоны", "Мобильные устройства", [product1, product2])

    assert Category.category_count == initial_categories + 1
    assert Category.product_count == initial_products + 2

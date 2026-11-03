from ecommerce.category import Category
from ecommerce.utils import load_categories_from_json


def test_load_categories_from_json():
    categories = load_categories_from_json("products.json")

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert categories[1].name == "Телевизоры"

    assert isinstance(categories[0], Category)
    assert isinstance(categories[1], Category)

    assert "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" in (
        categories[0].products
    )
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n" in (categories[0].products)
    assert "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n" in (
        categories[0].products
    )

    assert '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n' in categories[1].products

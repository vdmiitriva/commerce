from ecommerce.category import Category
from ecommerce.product import Product
from ecommerce.utils import load_categories_from_json


def test_load_categories_from_json():
    categories = load_categories_from_json("products.json")

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert categories[1].name == "Телевизоры"

    assert len(categories[0].products) == 3
    assert len(categories[1].products) == 1

    assert isinstance(categories[0], Category)
    assert isinstance(categories[0].products[0], Product)

    assert categories[0].products[0].name == "Samsung Galaxy C23 Ultra"
    assert categories[0].products[0].price == 180000.0
    assert categories[0].products[0].quantity == 5

from ecommerce.product import Product


def test_product_init():
    product = Product(
        "Samsung Galaxy",
        "256GB, серый цвет",
        180000.0,
        5,
    )

    assert product.name == "Samsung Galaxy"
    assert product.description == "256GB, серый цвет"
    assert product.price == 180000.0
    assert product.quantity == 5

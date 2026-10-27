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


def test_new_product():
    data = {
        "name": "Samsung",
        "description": "Смартфон",
        "price": 1000.0,
        "quantity": 2,
    }

    product = Product.new_product(data, [])

    assert product.name == "Samsung"
    assert product.description == "Смартфон"
    assert product.price == 1000.0
    assert product.quantity == 2


def test_new_product_merge():
    existing_product = Product("Samsung", "Смартфон", 1000.0, 2)
    data = {
        "name": "Samsung",
        "description": "Новая версия описания",
        "price": 1500.0,
        "quantity": 3,
    }

    product = Product.new_product(data, [existing_product])

    assert product is existing_product
    assert product.quantity == 5
    assert product.price == 1500.0


def test_price_setter():
    product = Product("Samsung", "Смартфон", 1000.0, 2)

    product.price = 2000.0

    assert product.price == 2000.0


def test_price_setter_invalid(capsys):
    product = Product("Samsung", "Смартфон", 1000.0, 2)

    product.price = 0

    assert product.price == 1000.0
    assert "Цена не должна быть нулевая или отрицательная" in capsys.readouterr().out


def test_price_setter_decrease_confirmed(monkeypatch):
    product = Product("Samsung", "Смартфон", 1000.0, 2)

    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 800.0

    assert product.price == 800.0


def test_price_setter_decrease_cancelled(monkeypatch):
    product = Product("Samsung", "Смартфон", 1000.0, 2)

    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 800.0

    assert product.price == 1000.0

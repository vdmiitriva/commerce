import pytest

from ecommerce.product import LawnGrass, Product, Smartphone


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


def test_product_str():
    product = Product("Samsung", "Смартфон", 80.0, 15)

    assert str(product) == "Samsung, 80 руб. Остаток: 15 шт."


def test_product_add():
    product1 = Product("Samsung", "Смартфон", 100.0, 2)
    product2 = Product("iPhone", "Смартфон", 200.0, 3)

    assert product1 + product2 == 800.0


def test_smartphone_init():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, серый цвет",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )

    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, серый цвет"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawn_grass_init():
    grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_smartphone_inherits_product():
    smartphone = Smartphone(
        "iPhone 15", "512GB", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )

    assert isinstance(smartphone, Product)
    assert str(smartphone) == "iPhone 15, 210000 руб. Остаток: 8 шт."


def test_lawn_grass_inherits_product():
    grass = LawnGrass(
        "Газонная трава",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )

    assert isinstance(grass, Product)
    assert str(grass) == "Газонная трава, 450 руб. Остаток: 15 шт."


def test_smartphone_add():
    smartphone1 = Smartphone("Samsung", "256GB", 1000.0, 2, 95.5, "S23", 256, "Серый")
    smartphone2 = Smartphone("iPhone", "512GB", 2000.0, 3, 98.2, "15", 512, "Белый")

    assert smartphone1 + smartphone2 == 8000.0


def test_lawn_grass_add():
    grass1 = LawnGrass("Трава 1", "Описание", 100.0, 2, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass(
        "Трава 2", "Описание", 200.0, 3, "США", "5 дней", "Темно-зеленый"
    )

    assert grass1 + grass2 == 800.0


def test_smartphone_add_lawn_grass():
    smartphone = Smartphone("Samsung", "256GB", 1000.0, 2, 95.5, "S23", 256, "Серый")
    grass = LawnGrass("Трава", "Описание", 100.0, 3, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError):
        smartphone + grass


def test_lawn_grass_add_smartphone():
    smartphone = Smartphone("Samsung", "256GB", 1000.0, 2, 95.5, "S23", 256, "Серый")
    grass = LawnGrass("Трава", "Описание", 100.0, 3, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError):
        grass + smartphone


def test_product_add_smartphone():
    product = Product("Товар", "Описание", 100.0, 2)
    smartphone = Smartphone("Samsung", "256GB", 1000.0, 2, 95.5, "S23", 256, "Серый")

    with pytest.raises(TypeError):
        product + smartphone

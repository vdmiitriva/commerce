from src.ecommerce.product import Product


class Category:
    name: str
    description: str
    products: list[Product]

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = products


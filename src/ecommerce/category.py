from ecommerce.product import Product


class Category:
    """Представляет категорию товаров."""

    name: str
    description: str
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Инициализирует категорию и список её товаров."""
        self.name = name
        self.description = description
        self.__products: list[Product] = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию и увеличивает счётчик товаров."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает товары категории в виде строки."""
        prod = []
        for product in self.__products:
            prod.append(
                f"{product.name}, {product.price} руб. "
                f"Остаток: {product.quantity} шт.\n"
            )
        return "".join(prod)

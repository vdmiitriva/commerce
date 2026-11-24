from ecommerce.category import Category
from ecommerce.product import Product


class CategoryIterator:
    """Позволяет последовательно перебирать товары категории."""

    def __init__(self, category: Category) -> None:
        """Инициализирует итератор товарами категории."""
        self.products: list[Product] = category.products_list
        self.index: int = 0

    def __iter__(self) -> "CategoryIterator":
        """Возвращает сам итератор."""
        return self

    def __next__(self) -> Product:
        """Возвращает следующий товар или завершает итерацию."""
        if self.index >= len(self.products):
            raise StopIteration

        product = self.products[self.index]
        self.index += 1
        return product

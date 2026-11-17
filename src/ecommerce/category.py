from ecommerce.base import BaseEntity
from ecommerce.exceptions import ZeroQuantityError
from ecommerce.product import Product


class Category(BaseEntity):
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
        try:
            if not isinstance(product, Product):
                raise TypeError("Можно добавлять только объекты класса Product")

            if product.quantity == 0:
                raise ZeroQuantityError(
                    "Товар с нулевым количеством не может быть добавлен"
                )

            self.__products.append(product)
            Category.product_count += 1

        except ZeroQuantityError as error:
            print(f"Ошибка: {error}")

        else:
            print(f"Товар {product.name} успешно добавлен в категорию")

        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self) -> str:
        """Возвращает текстовое представление товаров категории."""
        prod: list[str] = []
        for product in self.__products:
            prod.append(
                f"{product.name}, {product.price} руб. "
                f"Остаток: {product.quantity} шт.\n"
            )
        return "".join(prod)

    @property
    def products_list(self) -> list[Product]:
        """Возвращает копию списка товаров категории."""
        return self.__products.copy()

    def __str__(self) -> str:
        """Возвращает название категории и общее количество единиц товаров."""
        total_quantity: int = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: " f"{total_quantity} шт."

    def middle_price(self) -> float:
        """Возвращает среднюю цену товаров категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

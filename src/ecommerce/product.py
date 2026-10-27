class Product:
    """Представляет товар с названием, описанием, ценой и количеством."""

    name: str
    description: str
    quantity: int

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """Инициализирует товар с заданными характеристиками."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, d: dict, ex_products: list["Product"]) -> "Product":
        """Создаёт товар или обновляет существующий товар с таким же названием."""
        name = d["name"]
        description = d["description"]
        price = float(d["price"])
        quantity = int(d["quantity"])

        for product in ex_products:
            if product.name == name:
                product.quantity += quantity
                if product.price < price:
                    product.price = price
                return product

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Возвращает текущую цену товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Проверяет новую цену и при необходимости запрашивает подтверждение."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif hasattr(self, "_Product__price") and new_price < self.__price:
            answer = input(
                "Цена ниже прошлой.\n"
                "Если вы точно хотите изменить её, введите [y].\n"
                "Чтобы оставить прошлую цену, введите [n]. "
            )
            if answer == "y":
                self.__price = new_price
        else:
            self.__price = new_price

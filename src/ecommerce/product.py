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
        """Создаёт товар или обновляет существующий с таким же названием."""
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
        """Проверяет цену и запрашивает подтверждение при её снижении."""
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

    def __str__(self) -> str:
        """Возвращает название товара, цену и количество на складе."""
        return f"{self.name}, {self.price:g} руб. " f"Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Возвращает общую стоимость остатков двух товаров."""
        if type(other) == type(self):
            first_sum = self.quantity * self.price
            second_sum = other.quantity * other.price
            return first_sum + second_sum
        else:
            raise TypeError("Можно складывать только товары одного класса")


class Smartphone(Product):
    """Представляет смартфон."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализирует смартфон с заданными характеристиками."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Представляет газонную траву."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализирует газонную траву с заданными характеристиками."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

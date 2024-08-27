class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса"""
        # Название
        self.name = name
        # Описание
        self.description = description
        # Цена
        self.__price = price
        # Количество в наличии
        self.quantity = quantity

    def __str__(self):
        """ Отображает строковое значение в нужном формате(название товара, цена и количество)
        для геттера category -> Category -> products """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """ Полная стоимость всех товаров на складе """
        if type(other) is Product:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError

    @classmethod
    def new_product(cls, new_product_dict, *products_list):
        """Создает объекты класса Product"""
        # for product in products_list:
        #     if new_product_dict.get("name") == product.get("name"):
        #         name = new_product_dict.get("name")
        #         description = new_product_dict.get("description")
        #         quantity = new_product_dict.get("quantity") + product.get("quantity")
        #         if new_product_dict.get("price") >= product.get("price"):
        #             price = new_product_dict.get("price")
        #         else:
        #             price = product.get("price")
        #         # return Product(name, description, price, quantity)
        #     else:
        #         name = new_product_dict.get("name")
        #         description = new_product_dict.get("description")
        #         price = new_product_dict.get("price")
        #         quantity = new_product_dict.get("quantity")
        #         # return Product(name, description, price, quantity)
        return Product(**new_product_dict)

    @property
    def price(self):
        """Показывает цену"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Изменяет цену, проверяет, чтобы цена не была отрицательная, либо нулевая и меньше старой цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная!")
        else:
            if self.__price > new_price:
                input_price = input(
                    "Новая цена меньше старой! Введите 'y', чтобы поменять цену, или 'n' для отмены: "
                ).lower()
                if input_price == "y":
                    self.__price = new_price
            else:
                self.__price = new_price

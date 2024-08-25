class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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

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
    def new_product(cls, new_product_dict, ):
        """ Создает объекты класса Product """
        name = new_product_dict.get("name")
        description = new_product_dict.get("description")
        price = new_product_dict.get("price")
        quantity = new_product_dict.get("quantity")
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """ Показывает цену """
        return self.__price

    @price.setter
    def price(self, new_price):
        """ Изменяет цену """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

from src.base_category_order import BaseCategoryOrder


class Order(BaseCategoryOrder):
    """ Сообщается какой товар был куплен, количество купленного товара,
    итоговая стоимость(в заказе может быть только один товар) """

    name: str
    quantity: int
    price: float

    def __init__(self, name, quantity, price):
        """ Конструктор класса Order """
        # Наименование товара
        self.name = name
        # Количество товара
        self.quantity = quantity
        # Итоговая стоимость товара
        self.price = price

    def total_price(self):
        """ Итоговая стоимость заказа """
        return self.quantity * self.price

    def __str__(self):
        """ Выводит информацию о заказанном товаре """
        return f"Заказ: {self.name}, количество: {self.quantity} шт., итоговая стоимость: {self.total_price()} руб."


if __name__ == '__main__':
    ord1 = Order("Iphone 15", 2, 31000.0)
    print(ord1)

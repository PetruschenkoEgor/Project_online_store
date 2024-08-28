from src.product import Product


class Smartphone(Product):
    """Категория товаров со смартфонами"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Конструктор класса Smartphone"""
        super().__init__(name, description, price, quantity)
        # Производительность
        self.efficiency = efficiency
        # Модель
        self.model = model
        # Объем встроенной памяти
        self.memory = memory
        # Цвет
        self.color = color

    def __add__(self, other):
        """Полная стоимость всех товаров категории Смартфонов на складе"""
        if type(other) is Smartphone:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError

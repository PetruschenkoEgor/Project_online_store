from src.product import Product


class Smartphone(Product):
    """ Категория товаров со смартфонами """
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """ Конструктор класса Smartphone """
        super().__init__(name, description, price, quantity)
        # Производительность
        self.efficiency = efficiency
        # Модель
        self.model = model
        # Объем встроенной памяти
        self.memory = memory
        # Цвет
        self.color = color

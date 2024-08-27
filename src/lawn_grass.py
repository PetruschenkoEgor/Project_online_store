from src.product import Product


class LawnGrass(Product):
    """ Категория товаров с травой газанной """
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """ Конструктор класса LawnGrass """
        super().__init__(name, description, price, quantity)
        # Страна-производитель
        self.country = country
        # Срок прорастания
        self.germination_period = germination_period
        # Цвет
        self.color = color

    def __add__(self, other):
        """ Полная стоимость всех товаров категории Трава газонная на складе """
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

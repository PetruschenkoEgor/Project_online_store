class PrintMixin:
    """ Класс-миксин """
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        """ Вывод информации в консоль """
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"

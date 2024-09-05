class ZeroQuantityProduct(Exception):
    """ Класс ошибки: добавление товара с нулевым количеством """
    def __init__(self, message=None):
        super.__init__(message)

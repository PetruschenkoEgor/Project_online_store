class ProductIterator:
    def __init__(self, product_obj):
        self.category = product_obj
        self.index = 0

    def __iter__(self):
        """Возвращает итератор"""
        self.index = 0
        return self

    def __next__(self):
        """Возвращает следующий элемент последовательности"""
        if self.index < len(self.category.products_list):
            product = self.category.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration

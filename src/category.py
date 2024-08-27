from src.product import Product


class Category:
    """Класс для представления категорий продуктов"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__products = products

        # Количество категорий
        Category.category_count += 1
        # Количество товаров
        Category.product_count += len(products)

    def __str__(self):
        """ Общее количество продуктов категории(строковое значение) """
        return f"{self.name}, количество продуктов: {sum([product.quantity for product in self.__products])} шт."

    @property
    def products_(self):
        """ Геттер для __products """
        return self.__products

    def add_product(self, *args):
        """Добавление нового товара"""
        for arg in args:
            if type(arg) is Product:
                self.__products.append(arg)
                Category.product_count += 1

    @property
    def products(self):
        """Показывает товары"""
        # return '\n'.join([f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        #                   for product in self.__products])
        return '\n'.join([f"{str(product)}" for product in self.__products])

    @property
    def products_list(self):
        """Список товаров для проверки при добавлении нового товара(для new_product)"""
        return self.__products

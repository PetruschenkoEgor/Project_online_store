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

    @property
    def products_(self):
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
        # product_list = []
        for product in self.__products:
            # product_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
            print(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")

    @property
    def products_list(self):
        """Список товаров для проверки при добавлении нового товара(для new_product)"""
        return self.__products

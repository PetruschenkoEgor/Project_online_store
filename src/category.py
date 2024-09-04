from src.product import Product
from src.base_category_order import BaseCategoryOrder
from src.exceptions import ZeroQuantityProduct


class Category(BaseCategoryOrder):
    """Класс для представления категорий продуктов"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Конструктор класса Category"""
        # Название
        self.name = name
        # Описание
        self.description = description
        # Список товаров категории
        self.__products = products

        # Количество категорий
        Category.category_count += 1
        # Количество товаров
        Category.product_count += len(products)

    def __str__(self):
        """Общее количество продуктов категории(строковое значение)"""
        return f"{self.name}, количество продуктов: {sum([product.quantity for product in self.__products])} шт."

    @property
    def products_(self):
        """Геттер для __products"""
        return self.__products

    def add_product(self, *args):
        """Добавление нового товара"""
        for arg in args:
            if isinstance(arg, Product):
                try:
                    if arg.quantity == 0:
                        raise ZeroQuantityProduct("Нельзя добавлять товар с нулевым количеством")
                except ZeroQuantityProduct as e:
                    print(str(e))
                else:
                    self.__products.append(arg)
                    Category.product_count += 1
                    print("Товар добавлен успешно")
                finally:
                    print("Обработка добавления товара завершена")
            else:
                raise TypeError

    @property
    def products(self):
        """Показывает товары"""
        # return '\n'.join([f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        #                   for product in self.__products])
        return "\n".join([f"{str(product)}" for product in self.__products])

    @property
    def products_list(self):
        """Список товаров для проверки при добавлении нового товара(для new_product)"""
        return self.__products

    def middle_price(self):
        """ Подсчет среднего ценника всех товаров """
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return "0"

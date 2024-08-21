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
        self.products = products

        # Количество категорий
        Category.category_count += 1
        # Количество товаров
        # for product in products:
        #     Category.product_count += product.quantity
        Category.product_count += len(products)

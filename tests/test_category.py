import pytest

from src.category import Category
from src.product import Product


def test_category_init(category_1, product_1, product_2):
    """Тест на корректность инициализации объектов класса Category"""
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_1.products_) == 2
    assert category_1.products_ == ["product_1", "product_2"]
    assert category_1.category_count == 1
    assert category_1.product_count == 2


def test_add_product(product_1, product_2):
    """Тест на добавление нового товара"""
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
        "удобства жизни",
        ["product1", "product2", "product3"],
    )
    assert len(category1.products_) == 3
    category1.add_product(product_1)
    assert len(category1.products_) == 4
    category1.add_product(product_2)
    assert len(category1.products_) == 5


def test_products_property(products):
    """Тест на правильное отображение товаров"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                       5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций "
        "для удобства жизни",
        [product1, product2, product3],
    )
    assert category1.products == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. "
                                  "Остаток: 8 шт.\nXiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.")


def test_category_str(product_1):
    """ Тест на правильное отображение строкового значения """
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_iterator(product_iterator):
    """ Тест итератора """
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"

    with pytest.raises(StopIteration):
        next(product_iterator)

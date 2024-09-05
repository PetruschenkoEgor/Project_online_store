import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


@pytest.fixture
def product_1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                   5)


@pytest.fixture
def product_2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category_1():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций "
        "для удобства жизни",
        ["product_1", "product_2"],
    )


@pytest.fixture
def product_dict():
    return Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )


@pytest.fixture
def products():
    return [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
    ]


@pytest.fixture
def category_11():
    product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                        5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций "
        "для удобства жизни",
        [product_1, product_2],
    )


@pytest.fixture
def product_iterator(category_11):
    return ProductIterator(category_11)


@pytest.fixture
def smartphone_1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                      5, 95.5, "S23 Ultra", 256, "Серый")


@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2,
                      "15", 512, "Gray space")


@pytest.fixture
def lawn_grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                     "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США",
                     "5 дней", "Темно-зеленый")


@pytest.fixture
def product_4():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                   0)


@pytest.fixture
def category_111():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций "
        "для удобства жизни",
        [],
    )

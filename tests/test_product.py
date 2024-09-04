from unittest.mock import patch


def test_product_init(product_1):
    """Тест на корректность инициализации объектов класса Product"""
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_product_new_product(product_dict):
    """Тест на корректность добавления нового продукта"""
    assert product_dict.name == "Samsung Galaxy S23 Ultra"
    assert product_dict.description == "256GB, Серый цвет, 200MP камера"
    assert product_dict.price == 180000.0
    assert product_dict.quantity == 5


def test_product_price_property(product_dict):
    """Тест - геттер"""
    assert product_dict.price == 180000.0
    assert product_dict.name == "Samsung Galaxy S23 Ultra"
    assert product_dict.description == "256GB, Серый цвет, 200MP камера"
    assert product_dict.quantity == 5


def test_product_price_setter_negative(capsys, product_dict):
    """Тест - сеттер(отрицательная цена)"""
    new_product = product_dict
    new_product.price = -800
    message = capsys.readouterr()
    assert new_product.price == 180000.0
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная!"


@patch("builtins.input", return_value="n")
def test_product_price_setter_less(mock_input, product_dict):
    """Тест - сеттер(новая цена меньше предыдущей)"""
    new_product = product_dict
    new_product.price = 800
    assert new_product.price == 180000.0


@patch("builtins.input", return_value="y")
def test_product_price_setter_less_(mock_input, product_dict):
    """Тест - сеттер(новая цена меньше предыдущей)"""
    new_product = product_dict
    new_product.price = 800
    assert new_product.price == 800


def test_product_price_setter_more(product_dict):
    """Тест - сеттер(цена больше)"""
    new_product = product_dict
    new_product.price = 190000.0
    assert new_product.price == 190000.0


def test_product_str(category_11):
    """ Тест на правильное отображение строковой информации """
    assert str(category_11) == "Смартфоны, количество продуктов: 13 шт."


def test_product_add(product_1, product_2):
    """ Тест на правильное сложение стоимости всех товаров """
    assert product_1 + product_2 == 2580000.0

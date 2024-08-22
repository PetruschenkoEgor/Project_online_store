from unittest.mock import Mock, patch


def test_product_init(product_1):
    """Тест на корректность инициализации объектов класса Product"""
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_product_new_product(product_dict):
    """ Тест на корректность добавления нового продукта """
    assert product_dict.name == "Samsung Galaxy S23 Ultra"
    assert product_dict.description == "256GB, Серый цвет, 200MP камера"
    assert product_dict.price == 180000.0
    assert product_dict.quantity == 5


# @patch('src.product.input')
# def test_product_price(mock_input, product_dict):
#     """ Тест на корректное изменение цены """
#     product_dict.price = 800
#     mock_input.return_value = 'n'
#     assert product_dict.price == 180000.0

# @patch('src.product.input')
def test_product_price_negative(product_dict):
    """ Тест на корректное изменение цены """
    product_dict.price = 190000.0
    # mock_input.return_value = 'n'
    assert product_dict.price == 190000.0

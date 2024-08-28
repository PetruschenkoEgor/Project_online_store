import pytest


def test_smartphone_init(smartphone_1):
    """ Тест на корректность инициализации объектов класса Smartphone """
    assert smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_1.price == 180000.0
    assert smartphone_1.quantity == 5
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == "S23 Ultra"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Серый"


def test_smartphone_add_smartphone(smartphone_1, smartphone_2):
    """ Тест на правильное сложение экземпляров класса из класса Смартфоны """
    assert smartphone_1 + smartphone_2 == 2580000.0


def test_smartphone_add_no_smartphone(smartphone_1, lawn_grass_1):
    """ Тест на правильное сложение экземпляров класса не из класса Смартфоны """
    with pytest.raises(TypeError):
        result = smartphone_1 + lawn_grass_1

    with pytest.raises(TypeError):
        result = smartphone_1 + 1

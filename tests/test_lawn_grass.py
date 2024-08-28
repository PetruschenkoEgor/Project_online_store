import pytest


def test_lawn_grass_init(lawn_grass_1):
    """ Тест на корректность инициализации объектов класса Smartphone LawnGrass """
    assert lawn_grass_1.name == "Газонная трава"
    assert lawn_grass_1.description == "Элитная трава для газона"
    assert lawn_grass_1.price == 500.0
    assert lawn_grass_1.quantity == 20
    assert lawn_grass_1.country == "Россия"
    assert lawn_grass_1.germination_period == "7 дней"
    assert lawn_grass_1.color == "Зеленый"


def test_lawn_grass_add_lawn_grass(lawn_grass_1, lawn_grass_2):
    """ Тест на правильное сложение экземпляров класса из класса Трава газонная """
    assert lawn_grass_1 + lawn_grass_2 == 16750.0


def test_lawn_grass_add_no_lawn_grass(lawn_grass_1, smartphone_1):
    """ Тест на правильное сложение экземпляров класса не из класса Трава газонная """
    with pytest.raises(TypeError):
        result = lawn_grass_1 + smartphone_1

    with pytest.raises(TypeError):
        result = lawn_grass_1 + 1

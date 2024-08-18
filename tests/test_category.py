def test_category_init(category_1, product_1, product_2):
    """Тест на корректность инициализации объектов класса Category"""
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description ==
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_1.products == [product_1, product_2]
    assert category_1.count == 2
    assert category_1.product_count == 13

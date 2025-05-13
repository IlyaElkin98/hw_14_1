def test_category(category_1, category_2, product_1, product_2, product_3, product_4):
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_1.products == [product_1, product_2, product_3]

    assert category_2.name == "Телевизоры"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_2.products == [product_4]

    assert len(category_1.products) == 3
    assert len(category_2.products) == 1

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 4
    assert category_2.product_count == 4


"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_item():
    return Item('Часы с кукушкой', 7000, 100)


def test__repr__(test_item):
    assert repr(test_item) == "Item('Часы с кукушкой', 7000, 100)"


def test__str__(test_item):
    assert str(test_item) == 'Часы с кукушкой'


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 700_000


def test_apply_discount(test_item):
    Item.pay_rate = 0.1
    test_item.apply_discount()
    assert test_item.calculate_total_price() == 70_000


def test_name(test_item):
    test_item.name = 'Пылесос'
    assert test_item.name == 'Пылесос'
    with pytest.raises(Exception):
        test_item.name = 'Вакуумный пылесос'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('17.777') == 17

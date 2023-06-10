"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_item():
    return Item('Часы с кукушкой', 7000, 100)


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 700_000


def test_apply_discount(test_item):
    Item.pay_rate = 0.1
    test_item.apply_discount()
    assert test_item.calculate_total_price() == 70_000

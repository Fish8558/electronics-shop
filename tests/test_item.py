"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest
from config import CSV_PATH

@pytest.fixture
def test_item():
    return Item('fff', 100.0, 2)


def test_item_repr(test_item):
    assert repr(test_item) == "Item('fff', 100.0, 2)"


def test_item_str(test_item):
    assert str(test_item) == 'fff'


def test_item_init(test_item):
    assert test_item.name == 'fff'
    assert test_item.price == 100.0
    assert test_item.quantity == 2
    # assert 100 * 0.1 == 10


def test_apply_discount(test_item):
    test_item.pay_rate = 0.5
    test_item.apply_discount()
    assert test_item.price == 50


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 200.0


def test_name(test_item):
    test_item.name = 'iphone'
    assert test_item.name == 'iphone'
    test_item.name = 'iphoneXXXL1500'
    assert test_item.name == 'iphoneXXXL'


def test_string_to_number(test_item):
    assert type(test_item.string_to_number('3')) == int
    assert type(test_item.string_to_number('3.0')) == int
    assert type(test_item.string_to_number('3.3')) == int


def test_instantiate_from_csv(test_item):
    test_item.instantiate_from_csv(CSV_PATH)
    assert len(test_item.all) == 5

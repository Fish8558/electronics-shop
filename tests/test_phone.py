"""Тесты для модуля phone"""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def test_item1():
    return Item('Смартфон', 10000, 20)


@pytest.fixture
def test_phon1():
    return Phone('iPhone 14', 120_000, 5, 2)


def test_name(test_phon1):
    assert str(test_phon1) == 'iPhone 14'
    assert repr(test_phon1) == 'Phone(iPhone 14, 120000, 5, 2)'
    assert test_phon1.number_of_sim == 2

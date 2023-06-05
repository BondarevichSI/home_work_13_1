"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def product():
    return Item('Смартфон', 1000, 3)


def test_calculate_total_price(product):
    assert product.calculate_total_price() == 3000.0


def test_apply_discount(product):
    assert product.apply_discount() == 1000


def test_name(product):
    assert product.name == 'Смартфон'


def test_name_setter(product):
    product.name = 'СуперСмартфон'
    with pytest.raises(Exception):
        product.name(0)


def test_string_to_number(product):
    assert product.string_to_number('5') == 5
    assert product.string_to_number('5.5') == 5.5

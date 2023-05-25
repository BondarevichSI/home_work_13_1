"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def product():
    return Item("f", 1000, 3)


def test_calculate_total_price(product):
    assert product.calculate_total_price() == 3000.0


def test_apply_discount(product):
    assert product.apply_discount() == 1000

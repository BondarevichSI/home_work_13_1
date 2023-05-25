"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def product():
    return "f", 1000, 3


def test_calculate_total_price(product):
    assert Item.calculate_total_price(product) == 3000


def test_apply_discount(product):
    assert Item.apply_discount(product) == 1000

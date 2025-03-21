from decimal import Decimal

import pytest

from python_patterns.comportamental.strategy.pedido import Item, Pedido
from python_patterns.comportamental.strategy.promocao import (
    desconto_grande_pedido, desconto_item_repetido)


def test_adicionar_item():
    mac = Item('Mac', Decimal('9.32'), 2)
    pedido = Pedido()
    pedido.adicionar(mac)
    assert 1 == len(pedido._items)


@pytest.mark.parametrize(
    'items,subtotal',
    [
        (
            [Item('Mac', Decimal('9.32'), 2)],
            '18.64'
        ),
        (
            [
                Item('Mac', Decimal('9.32'), 2),
                Item('Galaxy', Decimal('1.02'), 3)
            ],
            '21.70'
        )
    ]
)
def test_subtotal(items, subtotal):
    pedido = Pedido()
    pedido.adicionar(*items)
    assert Decimal(subtotal) == pedido.subtotal()


@pytest.fixture
def pedido_item_repetido():
    pedido = Pedido()
    pedido.adicionar(Item('Mac', Decimal('100.00'), 10))
    return pedido


def test_total_sem_promocao(pedido_item_repetido: Pedido):
    assert Decimal('1000.00') == pedido_item_repetido.total()


def test_total_com_desconto_por_item_repetido(pedido_item_repetido: Pedido):
    desconto = desconto_item_repetido
    assert Decimal('900.00') == pedido_item_repetido.total(desconto)


def test_total_sem_desconto_por_item_repetido(pedido_item_repetido: Pedido):
    pedido = Pedido()
    pedido.adicionar(Item('Mac', Decimal('100.00'), 9))
    desconto = desconto_item_repetido
    assert Decimal('900.00') == pedido.total(desconto)


def test_total_com_desconto_pedido_grande():
    pedido = Pedido()
    pedido.adicionar(Item('Mac', Decimal('10000.00'), 1))
    assert Decimal('9500.00') == pedido.total(desconto_grande_pedido)


def test_total_sem_desconto_pedido_grande():
    pedido = Pedido()
    pedido.adicionar(Item('Mac', Decimal('9999.99'), 1))
    assert Decimal('9999.99') == pedido.total(desconto_grande_pedido)

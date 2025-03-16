from decimal import Decimal

import pytest

from python_patterns.comportamental.strategy.pedido import Item, Pedido


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

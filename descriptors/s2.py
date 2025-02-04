import pytest


class ItemPedido:
    def __init__(self, descricao, preco, quantidade):
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor):
        if valor <= 0:
            raise TypeError('Quantidade deveria ser positiva')
        self._quantidade = valor

    def subtotal(self):
        return self.preco * self.quantidade


def test_subtotal():
    item = ItemPedido('Ervilha', 1.21, 2)
    assert item.subtotal() == pytest.approx(2.42)


def test_set_quantidade_negativa():
    item = ItemPedido('Ervilha', 1.21, 2)
    with pytest.raises(TypeError):
        item.quantidade = -2


def test_set_quantidade_negativa_no_init():
    with pytest.raises(TypeError):
        ItemPedido('Ervilha', 1.21, -2)


def test_set_preco_negativa():
    item = ItemPedido('Ervilha', 1.21, 2)
    with pytest.raises(TypeError):
        item.preco = -1.21


def test_set_preco_negativa_no_init():
    with pytest.raises(TypeError):
        ItemPedido('Ervilha', -1.21, 2)

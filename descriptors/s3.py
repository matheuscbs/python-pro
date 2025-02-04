import pytest


class Quantidade:
    def __init__(self):
        self._nome = f'_{id(self)}'

    def __get__(self, item, owner):
        return getattr(item, self._nome)

    def __set__(self, item, value):
        if value <= 0:
            raise TypeError('Quantidade deveria ser positiva')
        setattr(item, self._nome, value)


class ItemPedido:
    quantidade = Quantidade()
    preco = Quantidade()

    def __init__(self, descricao, preco, quantidade):
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

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

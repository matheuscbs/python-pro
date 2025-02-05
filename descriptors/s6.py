import pytest


class Quantidade:
    def __init__(self):
        self._nome = None

    def set_nome(self, nome: str):
        """Define o nome do atributo onde os valores serão armazenados"""
        self._nome = f'_{nome}'

    def __get__(self, item, owner):
        if self._nome is None:
            raise AttributeError("O nome do atributo ainda não foi definido pelo set_nome()")
        return getattr(item, self._nome)

    def __set__(self, item, valor):
        if self._nome is None:
            raise AttributeError("O nome do atributo ainda não foi definido pelo set_nome()")
        if valor <= 0:
            raise TypeError('Quantidade deveria ser positiva')
        setattr(item, self._nome, valor)


class _ModeloMeta(type):
    def __init__(self, cls_name, bases, propriedades):
        for nome, valor in propriedades.items():
            if isinstance(valor, Quantidade):
                valor.set_nome(nome)
        super().__init__(cls_name, bases, propriedades)


class ItemPedido(metaclass=_ModeloMeta):
    quantidade = Quantidade()
    preco = Quantidade()

    def __init__(self, descricao, preco, quantidade):
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.preco * self.quantidade


# Testes

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


def test_set_preco_negativo():
    item = ItemPedido('Ervilha', 1.21, 2)
    with pytest.raises(TypeError):
        item.preco = -1.21


def test_set_preco_negativo_no_init():
    with pytest.raises(TypeError):
        ItemPedido('Ervilha', -1.21, 2)


def test_propriedade_de_descriptor():
    item = ItemPedido('Ervilha', 1.21, 2)
    assert {'descricao': 'Ervilha', '_preco': 1.21,
            '_quantidade': 2} == item.__dict__

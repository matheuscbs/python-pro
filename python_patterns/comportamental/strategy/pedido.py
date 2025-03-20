from abc import ABC, abstractmethod
from decimal import Decimal


class Item:
    def __init__(self, descricao, preco, quantidade):
        self.preco = preco
        self.descricao = descricao
        self.quantidade = quantidade

    def total(self):
        return self.preco * self.quantidade


class Pedido:
    def __init__(self):
        self._items = []
        self._promocao = None

    def adicionar(self, *item):
        self._items.extend(item)

    def subtotal(self):
        return sum(item.total() for item in self._items)

    def total(self, promocao=None):
        """Retornar o valor do subtotal depois de aplicado o desconto

        :return: Decimal
        """
        if promocao is None:
            return self.subtotal()
        return promocao.calcular_desconto(self)

    def soma_dos_items_quantidade_maior_que(self, limite):
        return sum(
            item.total() for item in self._items
            if item.quantidade >= limite
        )


class Desconto(ABC):
    """Classe base de todos os descontos"""
    @abstractmethod
    def calcular_desconto(self, pedido: Pedido):
        """Deve calcular o valor de desconto de acordo com o pedido."""


class DescontoItemRepetido:
    """ Fornece 10% de desconto em cima de items com quantidade
    igual ou seperior a 10

    """
    def calcular_desconto(self, pedido):
        desconto = pedido.soma_dos_items_quantidade_maior_que(10)
        desconto *= Decimal('0.10')
        return pedido.subtotal() - desconto

from abc import ABC, abstractmethod
from decimal import Decimal


class Desconto(ABC):
    """Classe base de todos os descontos"""
    @abstractmethod
    def calcular_desconto(self, pedido):
        """Deve calcular o valor de desconto de acordo com o pedido."""


class _DescontoNullObject:
    def calcular_desconto(self, pedido):
        return pedido.subtotal()


desconto_null_object = _DescontoNullObject()


class _DescontoItemRepetido(Desconto):
    """ Fornece 10% de desconto em cima de items com quantidade
    igual ou seperior a 10

    """
    def calcular_desconto(self, pedido):
        desconto = pedido.soma_dos_items_quantidade_maior_que(10)
        desconto *= Decimal('0.10')
        return pedido.subtotal() - desconto


class _DescontoGrandePedido(Desconto):
    def calcular_desconto(self, pedido):
        subtotal = pedido.subtotal()
        if subtotal < 10000:
            return subtotal
        return subtotal * Decimal('0.95')


desconto_item_repetido = _DescontoItemRepetido()

desconto_grande_pedido = _DescontoGrandePedido()

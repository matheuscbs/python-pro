from abc import ABC, abstractmethod
from decimal import Decimal

from python_patterns.comportamental.strategy.pedido import Pedido


class Desconto(ABC):
    """Classe base de todos os descontos"""
    @abstractmethod
    def calcular_desconto(self, pedido: Pedido):
        """Deve calcular o valor de desconto de acordo com o pedido."""


class _DescontoItemRepetido(Desconto):
    """ Fornece 10% de desconto em cima de items com quantidade
    igual ou seperior a 10

    """
    def calcular_desconto(self, pedido: Pedido):
        desconto = pedido.soma_dos_items_quantidade_maior_que(10)
        desconto *= Decimal('0.10')
        return pedido.subtotal() - desconto


desconto_item_repetido = _DescontoItemRepetido()

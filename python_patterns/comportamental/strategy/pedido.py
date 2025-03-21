from python_patterns.comportamental.strategy.promocao import \
    desconto_null_object


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

    def total(self, promocao=desconto_null_object):
        """Retornar o valor do subtotal depois de aplicado o desconto

        :return: Decimal
        """
        return promocao(self)

    def soma_dos_items_quantidade_maior_que(self, limite):
        return sum(
            item.total() for item in self._items
            if item.quantidade >= limite
        )

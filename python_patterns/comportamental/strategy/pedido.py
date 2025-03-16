from collections import namedtuple

Item = namedtuple('Item', 'descricao preco quantidade')


class Pedido:
    def __init__(self):
        self._items = []

    def adicionar(self, item):
        self._items.append(item)

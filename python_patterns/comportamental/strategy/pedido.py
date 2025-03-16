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

    def adicionar(self, *item):
        self._items.extend(item)

    def subtotal(self):
        return sum(item.total() for item in self._items)

from decimal import Decimal


def desconto_null_object(pedido):
    return pedido.subtotal()


def desconto_item_repetido(pedido):
    """ Fornece 10% de desconto em cima de items com quantidade
    igual ou seperior a 10

    """
    desconto = pedido.soma_dos_items_quantidade_maior_que(10)
    desconto *= Decimal('0.10')
    return pedido.subtotal() - desconto


def desconto_grande_pedido(pedido):
    """Desconto de 5% para pedido maiores que 10.000"""
    subtotal = pedido.subtotal()
    if subtotal < 10000:
        return subtotal
    return subtotal * Decimal('0.95')

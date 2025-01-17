class Arvore:
    """
        >>> for noh in Arvore(0, Arvore(-2, Arvore(-4), Arvore(-1)), Arvore(10)):
        ...     print(noh)
        -4
        -2
        -1
        0
        10
    """
    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

    def __iter__(self):
        if self.esquerda is not None:
            yield from self.esquerda
        yield self.valor
        if self.direita is not None:
            yield from self.direita

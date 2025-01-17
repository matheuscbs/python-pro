class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return 'Carta(valor=%r, naipe=%r)' % (self.valor, self.naipe)


if __name__ == '__main__':
    print(Carta('A', '♣'))

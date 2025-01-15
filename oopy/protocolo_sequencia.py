from collections import Sequence


class Trem(Sequence):
    def __init__(self, num_vagoes):
        self.num_vagoes = num_vagoes

    def __len__(self):
        return self.num_vagoes

    def __getitem__(self, pos):
        indice = pos if pos >= 0 else self.num_vagoes + pos
        if 0 <= indice < self.num_vagoes:
            # indice 2 -> vagao #3
            return 'vagao #%s' % (indice + 1)
        raise IndexError('vagao inexistente %s' % pos)


if __name__ == '__main__':
    for vagao in Trem(4):
        print(vagao)

"""
O protocolo de sequência permite que uma classe personalizada
funcione como uma sequência em Python. Ao implementar os métodos
obrigatórios __len__ e __getitem__, a classe Trem pode ser iterada
com um for, ter seu comprimento consultado com len(), e
acessar elementos individuais com índices positivos e negativos,
como uma lista.
Esse comportamento é útil quando você quer criar tipos
personalizados de sequência que se comportem como listas ou tuplas,
mas com funcionalidades específicas.
"""

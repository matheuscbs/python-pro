import abc


class Bicicleta(abc.ABC):
    _marca = 'Caloi'

    def __init__(self):
        self._velocidade = 0

    @classmethod
    def marca(cls):
        return cls._marca

    @staticmethod
    def rodas():
        return 2

    @property
    def velocidade(self):
        print('velocidade')
        return self._velocidade

    @velocidade.setter
    def velocidade(self, valor):
        if valor >= 0:
            self._velocidade = valor
        else:
            self._velocidade = 0

    @abc.abstractmethod
    def pedalar(self):
        """Cada classe concreta deve definir
        o método pedalar com seu incremento na velocidade"""

    @abc.abstractmethod
    def frear(self):
        """Cada classe concreta deve definir
        o método pedalar com seu incremento na velocidade"""


class Monark(Bicicleta):
    _marca = 'Monark'

    def pedalar(self):
        self._velocidade += 10

    def frear(self):
        self._velocidade -= 3


if __name__ == '__main__':
    bicicleta = Monark()
    print(Bicicleta.marca())
    bicicleta.pedalar()
    bicicleta.frear()
    bicicleta.frear()
    bicicleta.frear()
    bicicleta.frear()
    # bicicleta.velocidade = -4  # acessando o endereço de memória
    # e passando um valor não permitido
    print(bicicleta.velocidade)
    print(Monark.marca())
    print(Monark.rodas())

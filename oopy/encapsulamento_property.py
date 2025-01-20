class Bicicleta:
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

    def pedalar(self):
        raise NotImplementedError()

    def frear(self):
        raise NotImplementedError()


class Monark(Bicicleta):
    _marca = 'Monark'

    def pedalar(self):
        self._velocidade += 10

    def frear(self):
        self._velocidade -= 3


if __name__ == '__main__':
    bicicleta = Bicicleta()
    print(Bicicleta.marca())
    bicicleta.pedalar()
    bicicleta.frear()
    bicicleta.frear()
    bicicleta.frear()
    bicicleta.frear()
    # bicicleta.velocidade = -4  # acessando o endereço de memória e passando um valor não permitido
    print(bicicleta.velocidade)
    print(Monark.marca())
    print(Monark.rodas())

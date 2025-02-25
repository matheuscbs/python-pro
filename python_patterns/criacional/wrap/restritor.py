class Cao:
    def __init__(self, nome, raca, sexo):
        self._sexo = sexo
        self.raca = raca
        self.nome = nome

    def latir(self):
        return 'Au'


class EmbrulhoRestritor:
    def __init__(self, embrulhado):
        self._embrulhado = embrulhado

    def __getattr__(self, nome):
        if nome.startswith('_'):
            raise AttributeError(f'Não é possível acessar atributo protegido: {nome}')
        return getattr(self.embrulhado, nome)


if __name__ == '__main__':
    rex = Cao('Rex', 'Vira Lata', 'Macho')
    print(rex.nome, rex.raca, rex.sexo)

    rex_restritor = EmbrulhoRestritor(rex)
    print(rex.__dict__)
    print(rex_restritor.latir())
    print(rex_restritor.nome)
    print(rex_restritor._sexo)

    Fiona = Cao('Rex', 'Beagle', 'Femea')

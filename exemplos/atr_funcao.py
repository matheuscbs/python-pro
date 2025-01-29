nome = 'Matheus'


def f(a: int, b: int = 2, *, c: str = '3') -> str:
    """Funcao exemplo para verificar atributos"""
    print(nome)
    return nome


f.parametro_dinamico = True


if __name__ == '__main__':
    print(f.__name__)
    print(f.__defaults__)
    print(f.__globals__)
    print(f.__dict__)
    print(f.__closure__)
    print(f.__annotations__)
    f(1, b=5, c='7')
    print(f.__kwdefaults__)

from .registrador import get_marcadas, marcar

# Import relativo e uso poetry run python -m programacao_funcional.decorador.funcoes_marcadas


def primeira():
    pass


primeira = marcar(primeira)


@marcar
def segunda():
    pass


if __name__ == '__main__':
    for f in get_marcadas():
        print(f.__name__)
    primeira()
    segunda

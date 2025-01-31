import functools
from functools import partial
from time import strftime


def logar(func=None, *, fmt='%H:%M:%S'):
    if func is None:
        return partial(logar, fmt=fmt)

    @functools.wraps(func)
    def envoltoria(*args, **kwargs):
        agora = strftime(fmt)
        print(f'{agora} executado função {func.__name__}')
        return func(*args, **kwargs)

    return envoltoria


# class logar:
#     def __init__(self, fmt):
#         self.fmt = fmt

#     def __call__(self, func):
#         @functools.wraps(func)
#         def envoltoria(*args, **kwargs):
#             agora = strftime('%H:%M:%S')
#             print(f'{agora} executado função {func.__name__}')
#             return func(*args, **kwargs)

#         return envoltoria


def ola_mundo():
    """Função olá mundo"""
    return 'Olá Mundo'


decorator = logar('%H:%M:%S')
ola_mundo = decorator(ola_mundo)  # type: ignore


@logar
def hello(nome):
    return f'Hello {nome}'


if __name__ == '__main__':
    print(ola_mundo())
    print(ola_mundo.__name__)
    print(ola_mundo.__doc__)
    print(hello('Matheus'))
    print(hello.__name__)

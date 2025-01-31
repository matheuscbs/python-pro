"""
Implementação do sistema de rotas simplificado inspirado no Flask
"""

# Dicionário para armazenar as rotas registradas
_rotas = {}


class RotaInexistente(Exception):
    """Exceção para quando uma rota não for encontrada."""
    def __init__(self, path):
        super().__init__(f'Rota inexistente: {path}')


def rota(path):
    """Decorator para registrar uma função como uma rota"""
    def decorator(func):
        _rotas[path] = func
        return func
    return decorator


def rotear(path, *args, **kwargs):
    """Executa a função correspondente à rota informada."""
    if path not in _rotas:
        raise RotaInexistente(path)

    return _rotas[path](*args, **kwargs)

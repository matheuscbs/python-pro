import pytest

from tombola.tombola import Tombola


@pytest.fixture
def tombola():
    return Tombola()


def test_carregar_e_carregada(tombola):
    # Verifica se a tombola inicialmente está vazia
    assert not tombola.carregada()

    # Carrega itens e verifica se está carregada
    tombola.carregar(["A", "B", "C"])
    assert tombola.carregada()


def test_sortear(tombola):
    tombola.carregar(["A", "B", "C"])
    tombola.misturar()

    # Sorteia itens e verifica que estão na lista original
    sorteado = tombola.sortear()
    assert sorteado in ["A", "B", "C"]

    # Verifica se o item foi removido
    assert sorteado not in tombola.itens

    # Sorteia até esvaziar
    tombola.sortear()
    tombola.sortear()
    assert not tombola.carregada()


def test_misturar(tombola):
    tombola.carregar(["A", "B", "C", "D", "E"])
    antes = tombola.itens[:]

    # Mistura os itens
    tombola.misturar()
    depois = tombola.itens

    # Garante que a lista foi embaralhada
    assert sorted(antes) == sorted(depois)
    assert antes != depois  # Em raras execuções, pode coincidir


def test_sortear_vazia(tombola):
    with pytest.raises(IndexError):  # A lista vazia gera IndexError ao tentar remover
        tombola.sortear()


def test_callable_tombola(tombola):
    tombola.carregar(["A", "B", "C"])

    # Verifica se o método __call__ funciona como esperado
    sorteado = tombola()
    assert sorteado in ["A", "B", "C"]
    assert sorteado not in tombola.itens


def test_carregar_multiplas_vezes(tombola):
    # Carrega itens em etapas
    tombola.carregar(["A", "B"])
    tombola.carregar(["C", "D"])

    assert len(tombola.itens) == 4
    assert "A" in tombola.itens
    assert "D" in tombola.itens

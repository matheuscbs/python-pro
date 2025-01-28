from itertools import product


def gerar_linha(matriz, n):
    return matriz[n]


def gerar_coluna(matriz, n):
    return [linha[n] for linha in matriz]


class Matriz:
    def __init__(self, lista):
        self.lista = lista

    def __matmul__(self, other):
        primeira = self.lista
        segunda = other.lista
        n_resultado_colunas = len(segunda[0])
        n_resultado_linhas = len(primeira)
        resultado = [[0 for _ in range(n_resultado_colunas)]
                     for _ in range(n_resultado_linhas)]

        for i, j in product(range(n_resultado_linhas),
                            range(n_resultado_colunas)):
            for ele_linha, ele_coluna in zip(gerar_linha(primeira, i),
                                             gerar_coluna(segunda, j)):
                resultado[i][j] += ele_linha * ele_coluna

        return Matriz(resultado)

    def __repr__(self):
        return 'Matriz({})'.format(self.lista)


if __name__ == '__main__':
    matriz = [[1, 2],
              [3, 4]]

    for i in range(2):
        print('linha', i, gerar_linha(matriz, i))
        print('coluna', i, gerar_coluna(matriz, i))

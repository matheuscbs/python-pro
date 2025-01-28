# Criando classe matriz que sobrecarrega multiplicacao de Matrizes

Deve ser possível criar duas matrizes

```python
  >>> from matriz import Matriz
  >>> m1 = Matriz([[1], [2]])  # Matriz 2x1
  >>> m2 = Matriz([[3, 4]])  # Matriz 1x2

```

Deve ser possível multiplicar Matrizes onde o número de colunas da primeira é igual ao número de linhas da segunda

```python
  >>> m1 @ m2
  Matriz([[3, 4], [6, 8]])
  >>> Matriz([[1, 2], [3, 4]]) @ Matriz([[1, 2], [3, 4]])
  Matriz([[7, 10], [15, 22]])

```

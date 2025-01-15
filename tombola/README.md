# TDD da Tombola

Uma tombola pode ser criada da seguinte maneira:

```python
    >>> from tombola import tombola
    >>> t = tombola.Tombola()

```

Após a criação os items da tombola são repersentados por uma lista vazia:

```python
    >>> t.itens
    []

```

Uma lista recém criada não possui elementos. Portanto, o método "carregada""
retorna falso:

```python
    >>> t.carregada()
    False

```

É possível carregar itens através do método "carregar"

```python
    >>> itens = [1, 2]
    >>> t.carregar(itens)
    >>> t.itens
    [1, 2]

```

Após ser carregada o método "carregada" retorna verdadeiro:

```python
    >>> t.carregada()
    True

```

Uma tombola pode misturar os seus items:

```python
    >>> def embaralhador_mock(lista):
    ...     lista[0], lista[-1] = lista[-1], lista[0]
    >>> tombola.shuffle = embaralhador_mock
    >>> t.itens
    [1, 2]
    >>> t.misturar()
    >>> t.itens
    [2, 1]

```

Uma tombola serve para sortear elementos:

```python
    >>> t.sortear()
    1
    >>> t.carregada()
    True
    >>> t.sortear()
    2
    >>> t.carregada()
    False
    >>> itens
    [1, 2]

```

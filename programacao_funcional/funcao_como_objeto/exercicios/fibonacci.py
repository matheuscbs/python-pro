def fibonacci(n):
    """
      Retorna a sequência de Fibonacci até o n-ésimo termo.

      >>> fibonacci(6)
      [0, 1, 1, 2, 3, 5]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequencia = [0, 1]
    for i in range(2, n):
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


n = int(input("Digite o número de termos: "))
print(fibonacci(n))

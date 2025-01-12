'''
Construa uma função de ordenação que ordene os alunos por nota.
Se houver empate em nota, o nome deverá definir a ordem

>>> alunos = [("Matheus", 0), ("Katy", 10), ("Cardoso", 6), ("Barbosa", 10)]
>>> alunos.sort(key = ordenar_por_nota_e_nome)
>>> alunos
[("Barbosa", 10), ("Katy", 10), ("Cardoso", 6), ("Matheus", 0)]
'''

alunos = [("Matheus", 0), ("Katy", 10), ("Cardoso", 6), ("Barbosa", 10)]


def ordenar_por_nota_e_nome(aluno):
    nome, nota = aluno
    return (-nota, nome)


alunos_ordenados = sorted(alunos, key=ordenar_por_nota_e_nome)


print(
      "Alunos ordenados por ordem decrescente de nota e nome \n",
      alunos_ordenados
)

print(
    "Alunos ordenados por ordem decrescente de nota e nome \n",
    [(nome, nota) for nome, nota in sorted(alunos, key=lambda x: (-x[1], x[0]))]
)

print(
    "Alunos ordenados por ordem crescente de nota e nome \n",
    [(nome, nota) for nome, nota in sorted(alunos, key=lambda x: (x[1], x[0]))]
)

"""
Groupby - agrupando dados em python
"""

from itertools import groupby, tee

alunos = [
    {'nome': 'Rafael', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'José', 'nota': 'B'},
    {'nome': 'José Maria', 'nota': 'B'},
    {'nome': 'Josefina', 'nota': 'A'},
    {'nome': 'Joaquina', 'nota': 'A'},
    {'nome': 'Josélia', 'nota': 'A'},
    {'nome': 'Josimara', 'nota': 'A'},
    {'nome': 'Jose', 'nota': 'A'},
    {'nome': 'Clara', 'nota': 'B'},
    {'nome': 'Thaís', 'nota': 'B'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
# Em vez de usar o iterador, as cópias estão sendo usadas
# no lugar do iterador.
    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

# Nesse 'for' foi esgotado os valores do iterador.

    quantidade = len(list(va2))
# A segunda cópia foi usada

    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()

# O 'import' 'tee' faz duas cópias do iterador

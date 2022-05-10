"""
Groupby - agrupando dados em python
"""

from itertools import groupby

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
    print(f'Agrupamento: {agrupamento}')

    quantidade = len(list(valores_agrupados))
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')

# Faz a contagem do número de alunos conforme a nota que cada
# um recebeu.

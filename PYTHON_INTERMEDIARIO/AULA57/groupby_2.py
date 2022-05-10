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
    {'nome': 'José', 'nota': 'B'}
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')

    quantidade = len(list(valores_agrupados))
# Serve para contar a quantidade de alunos de acordo com a nota.
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')

# É necessário ordenar os valores, pois se isso não for feito
# o interpretador do python segue a ordem em que os dados
# estão registrados.

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

alunos.sort(key=lambda item: item['nota'])

for aluno in alunos:
    print(aluno)

# A função 'sort' é usada para ordenar as funções de
# acordo com algum critério. Nesse caso é o ‘item’ 'nota'.
# A função 'lambda' é uma função anônima dentro da 'sort'.


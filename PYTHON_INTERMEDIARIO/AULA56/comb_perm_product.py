"""
COmbinations, Permutations e Product - Itertools
Combinação — Ordem não importa
Permutação — Ordem importa
Ambos não repetem valores únicos
Produto — Ordem importa e repete valores únicos
"""

from itertools import combinations

pessoas = ['Rafael', 'André', 'Letícia', 'Eduardo', 'Fabrício', 'Rose']

for grupo in combinations(pessoas, 2):
    print(grupo)

# Usando 'combinations', as combinações não se repetem.


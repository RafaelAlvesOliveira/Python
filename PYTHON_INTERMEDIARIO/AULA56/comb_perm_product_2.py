"""
COmbinations, Permutations e Product - Itertools
Combinação — Ordem não importa
Permutação — Ordem importa
Ambos não repetem valores únicos
Produto — Ordem importa e repete valores únicos
"""

from itertools import product

pessoas = ['Rafael', 'André', 'Letícia', 'Eduardo', 'Fabrício', 'Rose']

for grupo in product(pessoas, repeat=2):
    print(grupo)

# Para ver todas as combinações possíveis, é necessário 'product'.


"""
COmbinations, Permutations e Product - Itertools
Combinação — Ordem não importa
Permutação — Ordem importa
Ambos não repetem valores únicos
Produto — Ordem importa e repete valores únicos
"""

from itertools import permutations

pessoas = ['Rafael', 'André', 'Letícia', 'Eduardo', 'Fabrício', 'Rose']

for grupo in permutations(pessoas, 2):
    print(grupo)

# Para 'permutations' a ordem importa, por isso o número de
# combinações é maior, por exemplo: 'Rafael', André não é a
# mesma coisa que 'André', 'Rafael. Essa é a diferença entre
# 'permutations' e 'combinations'.
# A permutação não faz combinações com itens iguais.


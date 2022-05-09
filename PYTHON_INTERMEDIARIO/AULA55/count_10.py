"""
Count - Itertolls
"""

from itertools import count

contador = count(start=9, step=-1)
# Nessa situação o contador é infinito, pois
# nunca atenderá a condição dentro do 'for'.
# E podem ser usados números negativos.

for valor in contador:
    print(round(valor, 2))

    if valor >= 10 or valor <= -10:
        break

# Foi feita essa alteração no 'if' para corrigir o
# problema da contagem infinita. Pois, se uma das
# condições for atendida, o laço é quebrado.


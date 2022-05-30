"""
Count - Itertolls
"""

from itertools import count

contador = count(start=5, step=2)
# Nesse caso, pode-se informar o interpretador
# que se quer pular a contagem a cada 2.

for valor in contador:
    print(valor)

    if valor >= 10:
        break



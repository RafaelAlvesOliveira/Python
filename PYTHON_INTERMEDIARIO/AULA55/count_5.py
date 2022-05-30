"""
Count - Itertolls
"""

from itertools import count

contador = count(start=5)
# O contador permite definir um valor inicial para
# começar a contagem.

for valor in contador:
    print(valor)

    if valor >= 10:
        break

# Pode-se definir um valor limite para que o
# contador pare quando chegar no valor informado.

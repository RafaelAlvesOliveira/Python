"""
Count - Itertolls
"""

from itertools import count

contador = count(start=5, step=0.1)
# Nesse caso também pode ser utilizado números
# de ponto flutuante.

for valor in contador:
    print(round(valor, 2))
# O número dois no parêntese do 'round' é
# para indicar o nível de precisão. Nesse caso,
# é de duas casas decimais.

    if valor >= 10:
        break



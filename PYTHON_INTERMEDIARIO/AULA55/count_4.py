"""
Count - Itertolls
"""

from itertools import count

contador = count()

for valor in contador:
    print(valor)

# Como o comando 'for' sempre irá pedir um novo
# valor para o contador e o contador vai continuar
# infinitamente a informar um novo valor. Fazendo
# com que esse processo se torne um laço infinito.

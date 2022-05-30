"""
Count - Itertolls
"""

from itertools import count

contador = count()
lista = ['Rafael', 'João', 'Maria', 'José', 'Eduardo', 'Sílvio']
# Não será necessário fazer nenhuma alteração no
# código, pois o python já tem contadores embutidos
# no próprio código.
lista = zip(contador, lista)
print(list(lista))



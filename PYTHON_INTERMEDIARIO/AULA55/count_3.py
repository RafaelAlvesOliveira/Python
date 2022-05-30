"""
Count - Itertolls
"""

from itertools import count

contador = count()

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

# Muito cuidado ao usador um gerador infinito, como
# é o caso de 'count'.

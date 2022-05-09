"""
Count - Itertolls
"""
from types import GeneratorType
variavel = ((x, y) for x, y in zip('Alo', 'Alo'))
# Nesse caso a 'variavel' é um gerador
print(isinstance(variavel, GeneratorType))
print(list(variavel))



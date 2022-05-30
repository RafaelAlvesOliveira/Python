"""
Dicionários em Python
"""

d1 = { 1: 'a', 2: 'b', 3: 'c', 'd': ['Rafael', 'Joana']}
v = d1.copy()

v[1] = 'Rafael'

print(v['d'][0])

print(d1)
print(v)

# Nesse caso é feita uma cópia do dicionário
# e todos os valores alterados na cópia, não
# são alterados na referência.

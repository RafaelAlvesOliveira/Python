"""
Dicionários em Python
"""

import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ('Rafael', 'Joana')}
v = d1.copy()

v[1] = 'Rafael'
v['d'] = ('Joana', 'Rafael')

print(d1)
print(v)


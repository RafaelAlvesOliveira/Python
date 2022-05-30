"""
Tuplas
"""

t1 = 1, 2, 'Rafael', 3, 4, 5,
t2 = 6, 7, 8, 9, 10
t3 = t1 + t2
print(t3)

n1, n2, n3, *_, n10 = t3

print(n10)

# É possível fazer o desempacotamento nas tuplas

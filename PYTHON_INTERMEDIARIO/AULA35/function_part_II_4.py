"""
Funções (def) em Python - return - Parte 2
"""


def f(var):
    print(var)


def dumb():
    return f


# Nesse caso 'var' é igual à função 'f',
# pois os dois tem o mesmo 'id' no sistema

var = dumb()
print(id(var), id(f))

if var == f:
    print('var é igual a f')
else:
    print('Blá Blá Bláblá')

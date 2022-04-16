"""
Expressões Lambda ou funções anônimas
"""


def funcao(arg, arg2):
    return arg * arg2


var = funcao(2, 2)
print(var)

anonima = lambda x, y: x * y
print(anonima(2, 2))
# A função lambda faz a mesma coisa que a outra função,
# a diferença é que é ela é anônima.

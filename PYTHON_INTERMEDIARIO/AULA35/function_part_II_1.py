"""
Funções (def) em Python - return - Parte 2
"""


def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2


divide = divisao(8, 2)

if divide:
    print(divide)
else:
    print('Conta inválida.')

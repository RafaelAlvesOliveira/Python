"""
Funções (def) em Python - *args **kwargs -
Aula 16 (Parte 3)
"""


def func(*args):
    args = list(args)  # Mudar 'args' usando 'casting' para transformá-lo em uma lista
    args[0] = 20
    print(args)


func(1, 2, 3, 4, 5)

"""
Funções (def) em Python - *args **kwargs - (Parte 3)
"""


def func(*args):
    for v in args:
        print(v)


# Se a lista não for desempacotada, o interpretador
# ira mostrar uma lista dentro de outra.

lista = 1, 2, 3, 4, 5
func(lista)


"""
Funções (def) em Python - *args **kwargs -
Aula 16 (Parte 3)
"""


def func(*args):
    for v in args:
        print(args)


# Se a lista não for desempacotada, o interpretador
# ira mostrar uma lista dentro de outra.

lista = [1, 2, 3, 4, 5]
func(lista, '6')

# Se a lista não estiver entre colchetes
# aparecerá uma tupla dentro de outra tupla.

"""
Funções (def) em Python - *args **kwargs - (Parte 3)
"""


def func(*args):
    print(args)
    # print(args[0])


# Se a lista não for desempacotada, o interpretador
# ira mostrar uma lista dentro de outra.
# Nesse caso as listas estão mescladas em um mesmo índice.

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2)

# A lista vai desempacotada e dessa forma faz parte dos
# índices da tupla
# O símbolo de '*' asterisco indica que a lista está
# desempacotada, e os elementos inseridos posteriormente
# farão parte da primeira lista '*args'.

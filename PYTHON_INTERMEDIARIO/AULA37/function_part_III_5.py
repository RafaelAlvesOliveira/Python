"""
Funções (def) em Python - *args **kwargs -
Aula 16 (Parte 3)
"""


def func(*args):
    print(args)     # Esse 'args' se refere a tupla inteira
    print(args[0])      # Nesse caso pode-se escolher algum índice no args, nesse caso o primeiro
    print(args[-1])     # O último valor que aparece no args, por isso o índice '-1'
    print(len(args))    # Usando a função 'len' pode-se saber quantos valores há dentro da tupla

# Tuplas diferentemente de listas, não pode ser alterada


func(1, 2, 3, 4, 5)

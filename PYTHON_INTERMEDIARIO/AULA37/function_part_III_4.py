"""
Funções (def) em Python - *args **kwargs -
Aula 16 (Parte 3)
"""


# Em muitos casos não se saberá o número de argumentos
# que serão repassados para a função, e nesses casos
# se usará o '*args'
# O 'args' é um equivalente de empacotamento e
# desempacotamento

def func(*args):
    print(args)


# Se for necessário acessar o '*args' é só incluir o
# (args) na função.

lista = [1, 2, 3, 4, 5]
print(*lista)
print(*lista, sep='-')

# O símbolo '*' na frente do nome lista serve
# para desempacotar cada valor na lista
# A função 'print' tem o argumento 'sep',
# usado para determinar como será feita a
# separação que deve haver entre os
# valores da lista.

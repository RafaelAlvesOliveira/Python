"""
Funções (def) em Python - *args **kwargs - (Parte 3)
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
n1, n2, *n = lista
print(n1, n2, n)

# Nesse exemplo está se desempacotando os primeiros
# dois valores e o restante está sendo empacotado
# na variável '*n', que armazena os valores restantes.

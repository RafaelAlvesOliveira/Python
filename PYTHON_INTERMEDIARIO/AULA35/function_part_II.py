"""
Funções (def) em Python - return - Parte 2
"""


# O valor 'None' representa nada em python
# Sempre que o interpretador encontra a palavra
# "return" a função é encerrada.

def funcao(var):
    return var


variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')

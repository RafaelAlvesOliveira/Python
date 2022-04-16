"""
Funções (def) em Python -  (Parte 4)
"""

variavel = 'valor'


def func():
    print(variavel)


def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg


# Se precisar de uma variável global na função e for
# necessário trabalhar o valor dela, pode-se
# usar um argumento

func()
outra_variavel = func2(arg=variavel)

print(outra_variavel)

# Também é possível reatribuir um valor em outra variável
# sem ser necessário alterar a variável global.

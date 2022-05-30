"""
1- Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor
da função2 executada.
"""


def funcao1():
    variavel = 'Rafael'
    return variavel


def funcao2(argumento):
    print(argumento)


arg = funcao1()
funcao2(arg)

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor
da função2 executada. Faça a função1 executar duas funções que recebem um
número diferente de argumentos.
"""


def func_mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def func_slave(nome):
    return f'Oi, meu nome é {nome}'


def func_slave2(sobrenome, idade):
    return f'Meu sobrenome é {sobrenome} e tenho {idade} anos.'


executar = func_mestre(func_slave, 'Rafael')
executar2 = func_mestre(func_slave2, 'Alves', idade=31)
print(executar)
print(executar2)

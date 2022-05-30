"""
Funções decoradoras e decoradores
"""


# A função 'master' recebe 'funcao' como parâmetro, e
# dentro dela foi definida a função 'slave', que tem o
# trabalho de executar a função que a 'master' recebe
# como parâmetro.

def master(funcao):
    def slave():
        funcao()
    return slave


def fala_oi():
    print('Oi')


variavel = master(fala_oi)
variavel()


# Resumindo ela recebe a função e executa.
# E a 'master' retorna a 'slave' sem executar ela.
# O print 'Oi' está vindo da função 'fala_oi', que a função
# 'master' recebeu como parâmetro e a 'slave' executou.


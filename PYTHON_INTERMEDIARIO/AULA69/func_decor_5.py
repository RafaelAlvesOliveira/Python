"""
Funções decoradoras e decoradores
"""


def master(funcao):
    def slave():
        print('Agora estou decorada.')
        funcao()
    return slave


def fala_oi():
    print('Oi')


fala_oi = master(fala_oi)
fala_oi()

# Ness contexto a função 'fala_oi' também é
# escrava da função 'master'.




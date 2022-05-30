"""
Funções decoradoras e decoradores
"""


def master(funcao):
    def slave():
        funcao()
    return slave


def fala_oi():
    print('Oi')


fala_oi = master(fala_oi)
fala_oi()

# Esse trecho de código é o equivalente a executar
# a função 'fala_oi' diretamente. A função 'fala_oi'
# foi decorada com a função master.



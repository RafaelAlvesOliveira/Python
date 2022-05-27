"""
Funções decoradoras e decoradores
"""


def master(funcao):
    def slave():
        funcao()
    return slave


def fala_oi():
    print('Oi')


# fala_oi = master(fala_oi)
fala_oi()

# Se a função 'fala_oi' for executada como mostrado
# acima, ela não estará 'decorada'.



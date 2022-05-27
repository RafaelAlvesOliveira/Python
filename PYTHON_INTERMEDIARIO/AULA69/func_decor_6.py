"""
Funções decoradoras e decoradores
"""

# Essa é uma função decoradora.
def master(funcao):
    def slave():
        print('Agora estou decorada.')
        funcao()
    return slave


# Isso é um decorador.
@master
def fala_oi():
    print('Oi')


fala_oi()

# Se quiser decorar a função 'master' ou qualquer outra
# função, pode se usar '@master' para fazer isso.





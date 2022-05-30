"""
Funções decoradoras e decoradores
"""

# A função decoradora é normalmente usada
# para adicionar algum recurso na função,
# ou, por exemplo, testar o tempo que uma
# função leva para ser executada.


# Essa é uma função decoradora.
def master(funcao):
    def slave(*args, **kwargs):
        print('Agora estou decorada.')
        funcao(*args, **kwargs)
    return slave


# Isso é um decorador.
@master
def fala_oi():
    print('Oi')


@master
def outra_funcao(msg):
    print(msg)


outra_funcao('Olá, eu sou Rafael.')

# Nesse caso, é gerado um erro informando que a
# função slave não recebe nenhum argumento posicional,
# mas um foi enviado. Para resolver isso, é necessário
# informar que a 'slave' vai receber '*args' e '**kwargs'.
# Ela vai repassar qualquer valor para a 'funcao' que
# seja decorada.


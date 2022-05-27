"""
Funções decoradoras e decoradores
"""


# As funções decoradoras vão envolver as funções
# que eu quiser, mudando ou não o comportamento
# delas conforme for necessário.


def fala_oi():
    print('Oi')


# fala_oi()
variavel = fala_oi
print(variavel)

# A função pode ser executada diretamente, ou pode-se
# usar uma variável que se comporta como função quando
# é invocada.


"""
Funções (def) em Python -  (Parte 4)
"""

variavel = 'valor'


# Não é posssível usar uma variável global na função
# trocar o valor dela e usar ela novamente, o interpretador
# enxerga primeiramente o valor atribuído a variável no
# contexto local
def func():
    print(variavel)
    variavel = 1234
    print(variavel)


# Não se pode alterar o valor de uma função global no
# contexto local sem informar ser uma variável global
func()

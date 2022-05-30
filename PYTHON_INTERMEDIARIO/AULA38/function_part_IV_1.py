"""
Funções (def) em Python -  (Parte 4)
"""
# Não é possível alterar uma variável global de
# dentro de uma função. Fazer isso não é considerado
# uma boa prática de programação.


variavel = 'valor'


def func():
    print(variavel)


def func2():
    global variavel
    variavel = 'Outro valor'
    print(variavel)


# se for necessário transformar uma variável local em
# global é necessário colocar 'global variavel' no
# escopo da função.

func()
func2()

print(variavel)

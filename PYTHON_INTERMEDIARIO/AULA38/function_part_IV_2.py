"""
Funções (def) em Python -  (Parte 4)
"""


variavel = 'valor'


def func():
    print(variavel)


def func2(arg=None):
    global variavel
    variavel = 'Outro valor'
    print(variavel)
    return arg

# Se for necessário usar variáveis na função, é
# só usar argumentos na função ou utilizar 'return'
# na função


func()
func2()

print(variavel)


"""
Funções (def) em Python -  (Parte 4)
"""

# Exemplo de como conectar duas funções sem ser
# necessário alterar o escopo global.


def func():
    outra_variavel = 'valor'
    return outra_variavel


# Para conseguir usar uma variável de escopo local
# em outra função, pode-se usar o 'return' para
# fazer isso.

def func2(arg):
    print(arg)


# Para fazer isso da forma correta, é necessário criar
# uma variável e atribuir o valor a algum 'arg' dentro
# da outra função, e imprimir o valor usando 'print'.

var = func()
func2(var)

"""
Funções (def) em Python -  (Parte 4)
"""

variavel = 'valor'


def func():
    outra_variavel = 'valor'


# Não é possível acessar uma variável que está no escopo
# local de outra função.

def func2():
    print(outra_variavel)


func()
func2()

# Se a 'func2()' for executada aparecerá um erro informando
# que a variável 'outra_variavel' não está definida.

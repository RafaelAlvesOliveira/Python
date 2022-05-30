"""
Funções (def) em Python -  (Parte 4)
"""

# Nesse caso a 'variavel' é declarada no escopo global
# Mas na 'func2()' ela é alterada no escopo local nesse
# caso da função

variavel = 'valor'


def func():
    print(variavel)


def func2():
    variavel = 'Outro valor'
    print(variavel)


func()
func2()

print(variavel)

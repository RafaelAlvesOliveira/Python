"""
While em Python
utilizando para realziar ações enquanto uma condição for verdadeira

Requisitos: Entender condições e operadores
"""

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue

# Nesse caso após o x ser igual a 3 o comando "continue" faz
# com que o interpretador ignore o trecho de código com o if
# e continua executando o while até que a condição seja satisfeita

    print(x)
    x = x + 1

print('Acabou!')

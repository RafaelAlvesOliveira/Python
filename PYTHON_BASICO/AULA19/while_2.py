"""
While em Python
utilizando para realziar ações enquanto uma condição for verdadeira

Requisitos: Entender condições e operadores
"""

x = 0
while x < 10:
    if x == 3:
        print(x)
        continue
# Nessa condição ele continua a repetir o número 3 infinitamente
    print(x)
    x = x + 1

print('Acabou!')

# Sempre for usada a palavra continue, ele irá pular o
# para o final e encerrará o while.

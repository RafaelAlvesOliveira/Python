"""
While em Python
utilizando para realziar ações enquanto uma condição for verdadeira

Requisitos: Entender condições e operadores
"""

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break

# O palavra "break" faz com que o trecho de código onde
# está seja encerra o while.

    print(x)
    x = x + 1

print('Acabou!')


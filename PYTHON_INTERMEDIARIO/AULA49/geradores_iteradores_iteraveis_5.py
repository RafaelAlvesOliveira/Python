"""
Geradores, iteradores e iteráveis
"""

import sys

lista = list(range(1000))

print(lista)
print(sys.getsizeof(lista))
# Esse comando serve para saber quantos 'bytes'
# de memória essa lista consume do meu
# computador.

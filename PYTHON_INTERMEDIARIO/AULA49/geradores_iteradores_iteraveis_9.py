"""
Geradores, iteradores e iteráveis
"""

import sys
import time


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()

print(next(g))


# Pode se usar a função next para mostrar os
# valores em cada iteração


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

print(g)
for v in g:
    print(v)

# A diferença entre o gerador e a lista do exemplo
# anterior é que a lista espera para retornar todos
# os valores já nesse caso o gerador faz isso com
# um valor por vez.


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

print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))


# Os iteradores ao contrário dos iteráveis tem o
# método '__next__'.
# Os iteradores também são iteráveis.


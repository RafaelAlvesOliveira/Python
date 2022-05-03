"""
Geradores, iteradores e iteráveis
"""

import sys
import time


l1 = [x for x in range(10000)]
l2 = (x for x in range(100000))
# print(next(l2))

for v in l2:
    print(v)


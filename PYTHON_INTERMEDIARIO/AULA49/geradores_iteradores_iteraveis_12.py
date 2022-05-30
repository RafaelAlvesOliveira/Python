"""
Geradores, iteradores e iteráveis
"""

import sys
import time


l1 = [x for x in range(10000)]
l2 = (x for x in range(10000))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))



"""
Geradores, iteradores e iteráveis
"""

import sys
import time


# lista = list(range(1000))
# Os dois representam a mesma coisa, contudo o
# formato a seguir é usando 'List Comprehension'.
lista = [x for x in range(1000)]
print(type(lista))  # Lista
lista = (x for x in range(1000))
print(type(lista))  # Gerador

# Essa é uma forma simplificada de criar um gerador.

print(sys.getsizeof(lista))

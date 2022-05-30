"""
Geradores, iteradores e iteráveis
"""

# Para descobrir se um objeto é iterável pode-se usar
# a função built-in do python 'hasattr'

lista = [0, 1, 2, 3, 4, 5]
lista1 = 1234
lista2 = 'String'

print(hasattr(lista, '__iter__'))
print(hasattr(lista1, '__iter__'))
print(hasattr(lista2, '__iter__'))

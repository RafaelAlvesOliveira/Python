"""
Geradores, iteradores e iteráveis
"""

# Um iterável é um objeto que se pode iterar
# sobre ele, mas ele não é um iterador, não
# necessariamente ele dará um valor de cada
# vez. Um iterador sempre dará um valor de
# cada vez, sempre que for necessário.

lista = [0, 1, 2, 3, 4, 5]
lista = iter(lista)

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista, '__next__'))


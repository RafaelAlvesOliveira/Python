"""
Geradores, iteradores e iteráveis
"""


lista = [0, 1, 2, 3, 4, 5]
lista = iter(lista)
print(hasattr(lista, '__next__'))

# Para que a lista se torne um iterador é necessário usar
# o método 'iter' como mostrado acima para que o método
# '__next__' retorne 'true'

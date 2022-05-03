"""
Geradores, iteradores e iteráveis
"""

# A maneira de saber se um determinado objeto
# ou item é um iterador

lista = [0, 1, 2, 3, 4, 5]

print(hasattr(lista, '__next__'))

# É preciso chegar o usando a função built-in
# 'hasattr' com o método '__next__'. Se a lista
# tivesse o método next ela seria um iterador.
